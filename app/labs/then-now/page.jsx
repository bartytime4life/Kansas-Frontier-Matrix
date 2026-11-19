import ThenNow from './ThenNow.jsx';
import crossing from './crossing.json';
import { bridgeInventoryHref, bridgeMarker } from './crossing.mjs';
import pair from './pair.json';

export const metadata = {
  title: 'Kansas Then & Now | Garden City',
  description: 'Compare two aligned aerial imagery editions of the Arkansas River crossing at Garden City, Kansas.',
};

export default function ThenNowPage() {
  return <ThenNow pair={pair} crossing={crossing} marker={bridgeMarker(crossing.location, pair.footprint.bounds)} inventoryHref={bridgeInventoryHref(crossing)}/>;
}
