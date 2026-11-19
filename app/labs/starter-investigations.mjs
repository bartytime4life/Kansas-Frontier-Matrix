import { currentSourceBindings, validateInvestigationState } from './investigation-state.mjs';
import { encodeWorkbenchView } from './workbench-view.mjs';

const countyState = Object.freeze({ countyA: '20173', countyB: '20091', mapMetric: 'medianIncome', xMetric: 'medianIncome', yMetric: 'populationChangePct', populationYear: 2025, acsYear: 2024, aqiYear: 2025, inventoryYear: 2026, rankOrder: 'desc', query: '', historyMetric: 'medianIncome', peerKeys: 'population,medianIncome,povertyPct,medianAge' });
export const NOTEBOOK_STARTERS = Object.freeze([
  Object.freeze({ id: 'county-change', title: 'Follow county change', workspace: 'county',
    question: 'How did population and poverty estimates differ between Finney and Riley counties?',
    coverage: 'Six population estimate years, 2020–2025; three ACS periods, 2010–2014, 2015–2019 and 2020–2024.',
    method: 'Inspect separate five-year estimates and their 90% margins of error. A visible difference is not a significance test.',
    state: Object.freeze({ ...countyState, countyA: '20055', countyB: '20161', mapMetric: 'povertyPct', historyMetric: 'povertyPct' }) }),
  Object.freeze({ id: 'comparison-county', title: 'Find a comparison county', workspace: 'county',
    question: 'Which counties have similar percentile positions to Sedgwick on population, income, poverty and age?',
    coverage: '105 Kansas counties; July 1, 2025 population estimates and 2020–2024 ACS estimates.',
    method: 'Inspect the common cohort, exclusions and each measure’s contribution, then select a candidate as county B. Uncertainty does not enter this descriptive distance.',
    state: countyState }),
  Object.freeze({ id: 'energy-changes', title: 'Separate energy trends', workspace: 'signal',
    question: 'How do annual changes in Kansas wind production and coal consumption vary together?',
    coverage: 'EIA annual Kansas series, 1990–2024; consecutive-year differences within that period.',
    method: 'Compare raw values with year-to-year differences and inspect the paired years. Overlapping energy accounts are not additive; association does not establish substitution or cause.',
    state: Object.freeze({ x: 'energy:SEDS.WYPRB.KS.A', y: 'energy:SEDS.CLTCB.KS.A', from: 1990, to: 2024, lag: 0, transform: 'difference', selectedYear: null }) }),
]);

export function starterInvestigationLink(id) {
  const starter = NOTEBOOK_STARTERS.find(entry => entry.id === id);
  if (!starter) throw new Error('Unknown starter investigation.');
  const state = validateInvestigationState(starter.workspace, starter.state);
  const token = encodeWorkbenchView({ workspace: starter.workspace, state, sourceBindings: currentSourceBindings(starter.workspace) });
  return `/labs/${starter.workspace === 'county' ? 'observatory' : 'signals'}?view=${token}`;
}

export function createStarterNotebook() {
  const createdAt = new Date().toISOString();
  const entries = NOTEBOOK_STARTERS.map(starter => ({ id: globalThis.crypto.randomUUID(), workspace: starter.workspace, title: starter.title, createdAt,
    state: validateInvestigationState(starter.workspace, starter.state), sourceBindings: currentSourceBindings(starter.workspace),
    notes: `Research question\n${starter.question}\n\nSource coverage\n${starter.coverage}\n\nMethod and limits\n${starter.method}\n\nEvidence I observed\n\nAlternative explanations\n\nNext check\n`,
  }));
  return JSON.stringify({ format: 'kfm-science-notebook-v1', exportedAt: createdAt, entries }, null, 2);
}
