import NewspaperPulse from './NewspaperPulse.jsx';

export const metadata = { alternates: { canonical: "https://kansasfrontiermatrix.com/labs/newspaper-pulse" },
  title: 'Newspaper Pulse | Kansas Frontier Matrix',
  description: 'Compare word matches in two digitized editions of the Abilene Weekly Reflector and open their original newspaper pages.',
};

export default function NewspaperPulsePage() {
  return <NewspaperPulse />;
}
