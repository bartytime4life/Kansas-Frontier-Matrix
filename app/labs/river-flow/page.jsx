import RiverFlow from './RiverFlow.jsx';
import { flowSettings } from './flow-model.mjs';
import { PUBLIC_SITE_ORIGIN } from '../../crawler-discovery';

export const metadata = {
  title: 'River Flow Lab | Kansas Frontier Matrix',
  description: 'Compare the frequency of high and low daily streamflow at three Kansas gauges using USGS records. See which dates match and download the evidence.',
  alternates: { canonical: `${PUBLIC_SITE_ORIGIN}/labs/river-flow` },
};

export default async function RiverFlowPage({ searchParams }) {
  return <RiverFlow initial={flowSettings(await searchParams)}/>;
}
