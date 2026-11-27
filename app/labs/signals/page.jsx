import SignalStudio from './SignalStudio.jsx';
import { PUBLIC_SITE_ORIGIN } from '../../crawler-discovery';

export const metadata = {
  title: 'Signal Studio | Kansas Frontier Matrix',
  description: 'Compare source-backed Kansas climate, energy, river and event signals by year. Inspect complete pairs, coverage, transformations and descriptive associations.',
  alternates: { canonical: `${PUBLIC_SITE_ORIGIN}/labs/signals` },
};

export default function SignalsPage() { return <SignalStudio/>; }
