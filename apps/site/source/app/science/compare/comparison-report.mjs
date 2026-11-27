import { csv, YEARS } from '../science-model.mjs';
import { comparisonPlace, DEFAULT_COMPARISON_PLACE } from './comparison-places.mjs';

const columns = [
  'schema', 'scope', 'comparison_place', 'selection_role', 'calendar_year', 'period', 'calendar_month',
  'metric_id', 'metric', 'measurement_kind', 'unit', 'place_id', 'place', 'geographic_support', 'time_standard',
  'value', 'support_state', 'valid_count', 'expected_count', 'support_unit', 'method', 'metric_limitation',
  'attribution', 'provider_documentation_url', 'lab_path', 'snapshot_url', 'snapshot_sha256', 'snapshot_bytes',
  'source_urls', 'source_capture_sha256', 'source_captured_at', 'provider_sources_json', 'comparison_limitations_json',
];

function selectionOf(report) {
  const selection = report?.selection;
  if (report?.schema !== 'kfm.science-comparison/v1' || report.scope !== 'provider-context' ||
      !Array.isArray(report.series) || report.series.length === 0 ||
      !YEARS.includes(selection?.year) || !YEARS.includes(selection?.compareYear) || selection.year === selection.compareYear) {
    throw new TypeError('Choose a completed science comparison.');
  }
  return selection;
}

function spreadsheetCell(value) {
  // Provider text can be interpreted as a formula even when CSV-quoted.
  // Preserve numeric values, including negative observations.
  return typeof value === 'string' &&
    (/^[\t\r\n]/.test(value) || /^[\s\p{Cf}\p{Cc}]*[=+@\-＝＋＠－]/u.test(value)) ? `'${value}` : value;
}

export function comparisonCsv(report) {
  const { year, compareYear } = selectionOf(report);
  const rows = [columns];
  const limitations = JSON.stringify(report.limitations);
  for (const series of report.series) {
    for (const [role, selectedYear] of [['selected', year], ['comparison', compareYear]]) {
      const sources = series.sources.filter((source) => source.year === selectedYear);
      const provenance = [series.attribution, series.documentation, series.labPath, series.display.url,
        series.display.sha256, series.display.bytes, sources.map((source) => source.url).join(' | '),
        sources.map((source) => source.sha256).join(' | '), sources.map((source) => source.capturedAt).join(' | '),
        JSON.stringify(sources)];
      for (const [month, point] of [[null, series.annual[role]], ...series.monthly.map((entry) => [entry.month, entry[role]])]) {
        const state = point.value === null ? 'unavailable' : point.valid < point.expected ? 'partial-support' : 'complete-support';
        rows.push([report.schema, report.scope, report.location.name, role, selectedYear, month === null ? 'annual' : 'monthly', month,
          series.id, series.label, series.kind, series.unit, series.location.id, series.location.name, series.location.scale, series.timeStandard,
          point.value, state, point.valid, point.expected, series.supportUnit, series.method, series.limitation, ...provenance, limitations]);
      }
    }
  }
  return csv(rows.map((row) => row.map(spreadsheetCell)));
}

export function comparisonJson(report) {
  selectionOf(report);
  return `${JSON.stringify(report, null, 2)}\n`;
}

export function comparisonExportFilename(report, extension) {
  const { year, compareYear } = selectionOf(report);
  if (extension !== 'csv' && extension !== 'json') throw new TypeError('Choose CSV or JSON.');
  const place = comparisonPlace(report.location?.id)?.id;
  const tag = place && place !== DEFAULT_COMPARISON_PLACE ? `${place}-` : '';
  return `kfm-science-comparison-${tag}${year}-vs-${compareYear}.${extension}`;
}
