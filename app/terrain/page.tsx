import TerrainView from './TerrainView';

export const metadata = {
  title: '3D Terrain · Konza Prairie | Kansas Frontier Matrix',
  description: 'Open a sampled historical Konza Prairie landscape in 3D. Compare ground, surface and independent canopy heights, inspect original readings and follow their source.',
  alternates: { canonical: 'https://kansasfrontiermatrix.com/terrain' },
};

export default function TerrainPage() { return <TerrainView/>; }
