import ThenNow from './ThenNow.jsx';
import pair from './pair.json';

export const metadata = {
  title: 'Kansas Then & Now | Garden City',
  description: 'Compare two aligned aerial imagery editions of the Arkansas River crossing at Garden City, Kansas.',
};

export default function ThenNowPage() {
  return <ThenNow pair={pair}/>;
}
