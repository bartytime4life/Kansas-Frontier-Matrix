import { STORIES } from '../living-welcome/stories/registry.mjs';
import { PUBLIC_LAB_SNAPSHOTS } from '../labs/public-snapshots.mjs';
import { atlasCoverage } from '../labs/atlas-model.mjs';

const workspaces = [
  { id: 'atlas-county-observatory', label: 'County Observatory', href: '/labs/observatory', topic: 'Reports & workspaces',
    question: 'Account for population change, compare county histories and peers, or bring a private CSV.', coverage: 'Kansas counties · coverage differs by indicator',
    source: 'U.S. Census, transportation and air records', keywords: 'county population change components births deaths migration balance remainder history poverty income education csv bridges' },
  { id: 'atlas-signals', label: 'Signal Studio', href: '/labs/signals', topic: 'Reports & workspaces',
    question: 'Compare annual signals and inspect the dates they share.', coverage: 'Kansas annual series · years vary by source',
    source: 'NOAA, USGS, EIA and other named sources', keywords: 'time series climate river flow water energy tornado correlation trend' },
  { id: 'atlas-notebook', label: 'Research notebook', href: '/labs/notebook', topic: 'Reports & workspaces',
    question: 'Open, organize, or export investigations saved on this device.', coverage: 'Browser-local saved investigations',
    source: 'Your saved KFM views and notes', keywords: 'saved notes report export reproducible workspace' },
  { id: 'atlas-grain', label: 'Grain markets & freight', href: '/science/wheat-trade', topic: 'Water & land',
    question: 'Compare crop delivery costs and trace changes in freight and trade.', coverage: 'Kansas bids and selected historical transport cases',
    source: 'USDA AMS and named transportation sources', keywords: 'agriculture farming wheat corn sorghum market rail export supply chain' },
].map(entry => ({ ...entry, kind: 'Workspace' }));

export function atlasScienceDirectory(native) {
  const entries = [...native, ...workspaces];
  const listed = new Set(entries.map(entry => entry.href));
  for (const story of STORIES) {
    const snapshot = Object.hasOwn(PUBLIC_LAB_SNAPSHOTS, story.id) ? PUBLIC_LAB_SNAPSHOTS[story.id] : null;
    if (story.status !== 'guided' && (story.status !== 'ready' || !snapshot)) continue;
    const href = story.href ?? '/labs?story=' + encodeURIComponent(story.id);
    if (listed.has(href)) continue;
    listed.add(href);
    entries.push({
      id: 'atlas-' + story.id, label: story.title, href, topic: story.group,
      question: story.summary,
      coverage: [atlasCoverage(snapshot), snapshot?.records ? snapshot.records.toLocaleString('en-US') + ' bundled source records' : null]
        .filter(Boolean).join(' · ') || 'Scope and dates in the lab',
      source: story.sources.join(', '),
      keywords: story.kicker,
      kind: 'Lab',
    });
  }
  return entries;
}
