import GhostTowns from './GhostTowns.jsx';
import { postalTimeline, readPostalView } from './post-office-model.mjs';
import snapshot from './post-office-snapshot.json';

export const metadata = {
  title: 'Boom & Ghost Towns | Kansas Frontier Matrix',
  description: 'Explore recorded post-office dates and approximate locations in Douglas County, Kansas.',
};

const timeline = postalTimeline(snapshot.records);

export default async function GhostTownsPage({ searchParams }: {
  searchParams: Promise<Record<string, string | string[] | undefined>>;
}) {
  const initial = readPostalView(await searchParams, timeline, snapshot.records);
  return <GhostTowns initial={initial}/>;
}
