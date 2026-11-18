import WaterChemistry from './WaterChemistry.jsx';
import snapshot from './water-snapshot.json';

export const metadata = {
  title: 'Water Chemistry | Kansas Frontier Matrix',
  description: 'Compare two source-linked dissolved nitrate sample windows at one Kansas river monitoring station.',
};

export default function WaterChemistryPage() {
  return <WaterChemistry snapshot={snapshot}/>;
}
