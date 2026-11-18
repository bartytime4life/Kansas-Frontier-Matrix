import DroughtReplay from './DroughtReplay.jsx';
import snapshot from './snapshot.json';

export const metadata = {
  title: '2012 Drought Replay | Kansas Frontier Matrix',
  description: 'Explore the 2012 drought in Finney County alongside daily Arkansas River discharge at Garden City.',
};

export default async function DroughtReplayPage({ searchParams }: {
  searchParams: Promise<{ week?: string | string[] }>;
}) {
  const { week } = await searchParams;
  return <DroughtReplay snapshot={snapshot} initialWeek={typeof week === 'string' ? week : undefined}/>;
}
