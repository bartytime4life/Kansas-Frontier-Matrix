import { PUBLIC_SITE_ORIGIN } from '../../crawler-discovery';
import EarthquakeLab from './EarthquakeLab.jsx';
import { catalogSettings } from './catalog-model.mjs';

export const metadata = {
  title: 'Earthquake Catalog Lab | Kansas Frontier Matrix',
  description: 'Compare the frequency, epicenters and reported depth of USGS catalog earthquakes around Kansas across four-year periods and magnitude thresholds.',
  alternates: { canonical: `${PUBLIC_SITE_ORIGIN}/labs/earthquakes` },
};

export default async function EarthquakePage({ searchParams }) {
  return <EarthquakeLab initial={catalogSettings(await searchParams)}/>;
}
