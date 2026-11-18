const RESULT = 'ResultMeasureValue';
const LIMIT = 'DetectionQuantitationLimitMeasure/MeasureValue';
const DATE = 'ActivityStartDate';
const BINS = 6;

export const waterLimits = [
  'The two windows cover equal calendar durations. Their sampled months and flow conditions differ.',
  'Distributions use quantified results. Non-detects retain the source reporting limit and are counted separately, without zero substitution.',
  'This is a comparison of selected surface-water records for one station. It supports a description of those samples and cannot establish a trend, a cause, or drinking-water compliance.',
];

const numericResult = record => record.status === 'numeric' ? Number(record.source[RESULT]) : null;
export const observationDate = record => record.source[DATE];
export const resultText = record => record.status === 'numeric' ? record.source[RESULT] : 'Not detected';
export const reportingLimit = record => record.source[LIMIT];
export const unitLabel = 'mg/L as N';

function periodSummary(period, records) {
  const numeric = records.flatMap(record => record.status === 'numeric' ? [numericResult(record)] : []).sort((a, b) => a - b);
  const dates = records.map(observationDate).sort();
  const middle = Math.floor(numeric.length / 2);
  const median = numeric.length === 0 ? null
    : numeric.length % 2 ? numeric[middle] : (numeric[middle - 1] + numeric[middle]) / 2;
  return {
    ...period,
    retained: records.length,
    quantified: numeric.length,
    nonDetects: records.length - numeric.length,
    median,
    sampledMonths: new Set(dates.map(value => value.slice(0, 7))).size,
    firstDate: dates[0] ?? null,
    lastDate: dates.at(-1) ?? null,
  };
}

export function waterComparison(snapshot) {
  const summaries = snapshot.periods.map(period => periodSummary(period, snapshot.records.filter(record => record.period === period.id)));
  const numeric = snapshot.records.filter(record => record.status === 'numeric');
  // Both windows use the same six decimal ranges and baseline. Select a human-readable step that includes the maximum.
  const maximum = Math.max(0, ...numeric.map(numericResult));
  const tenths = Math.max(1, Math.ceil(maximum * 10 / BINS));
  const bins = Array.from({ length: BINS }, (_, index) => ({
    lower: index * tenths / 10,
    upper: (index + 1) * tenths / 10,
    includeUpper: index === BINS - 1,
    records: [],
  }));
  for (const record of numeric) {
    const value = numericResult(record);
    const bin = bins.find(candidate => value < candidate.upper) ?? bins.at(-1);
    bin.records.push(record);
  }
  return { summaries, bins };
}

export function rangeLabel(bin) {
  return `${bin.lower} to ${bin.includeUpper ? '' : 'less than '}${bin.upper}${bin.includeUpper ? ' inclusive' : ''}`;
}

export function waterRecordSelection(snapshot, { period = 'all', interval = null, detection = 'all' } = {}) {
  const rows = interval ? interval.records : snapshot.records;
  return rows.filter(record => (period === 'all' || record.period === period)
    && (detection === 'all' || record.status === detection));
}

export function waterCsvRecords(records) {
  return [
    ['activity_id', 'period', 'activity_date', 'activity_time', 'source_time_zone', 'result_value', 'result_unit',
      'detection_condition', 'reporting_limit', 'reporting_limit_unit', 'qualifier', 'hydrologic_event'],
    ...records.map(({ activityId, period, source }) => [
      activityId, period, source[DATE], source['ActivityStartTime/Time'], source['ActivityStartTime/TimeZoneCode'],
      source[RESULT], source['ResultMeasure/MeasureUnitCode'], source.ResultDetectionConditionText,
      source[LIMIT], source['DetectionQuantitationLimitMeasure/MeasureUnitCode'], source.MeasureQualifierCode, source.HydrologicEvent,
    ]),
  ];
}

const markdownNumber = value => value === null ? 'Unavailable' : Number(value.toPrecision(4));
export function waterBrief(snapshot) {
  const { summaries } = waterComparison(snapshot);
  return [
    '# Water Chemistry | Kansas Frontier Matrix', '', `Station: ${snapshot.station.name} (${snapshot.station.id})`,
    '', '## Research question', '', 'How did reported dissolved nitrate values differ between these two sample windows?',
    '', '## Scope', '',
    'Dissolved nitrate as nitrogen, USGS parameter 00618, computed by the USGS NWIS ALGOR method. Routine surface-water samples collected by USGS method 15 with the US DH-81 sampler.',
    '', '| Period | Retained samples | Quantified | Non-detects | Sampled months | Median of quantified results |',
    '| --- | ---: | ---: | ---: | ---: | ---: |',
    ...summaries.map(period => `| ${period.label} | ${period.retained} | ${period.quantified} | ${period.nonDetects} | ${period.sampledMonths}/24 | ${markdownNumber(period.median)} ${unitLabel} |`),
    '', '## Source records', '',
    `- [Provider station](${snapshot.station.url})`,
    `- [Water Quality Portal result query](${snapshot.sources.results.url})`,
    `- Snapshot retrieved ${snapshot.sources.results.retrievedAt} UTC, SHA-256 \`${snapshot.sources.results.sha256}\`.`,
    ...summaries.map(period => `- ${period.label} activity identifiers: ${snapshot.records.filter(record => record.period === period.id).map(record => record.activityId).join(', ')}.`),
    '', '## Interpretation limits', '', ...waterLimits.map(limit => `- ${limit}`),
    '', `Source credit: ${snapshot.credit.name}.`, '',
  ].join('\n');
}
