import { PUBLIC_SITE_ORIGIN } from '../../crawler-discovery';
import TornadoSeason from './TornadoSeason.jsx';
import { seasonSettings } from './season-model.mjs';

export const metadata = {
  title: 'Tornado Season Lab | Kansas Frontier Matrix',
  description: 'Compare the months with the most Kansas-start tornado tracks and the most tornado days. Inspect NOAA records, mapped starts and reported endpoints.',
  alternates: { canonical: `${PUBLIC_SITE_ORIGIN}/labs/tornado-season` },
};

export default async function TornadoSeasonPage({ searchParams }) {
  return <TornadoSeason initial={seasonSettings(await searchParams)}/>;
}
