import type { Metadata } from 'next';
import CuratedWorkspace from './workspace';
export const metadata: Metadata = { title: 'Curated snapshots · Kansas Frontier Matrix' };
export default function CuratedPage() { return <CuratedWorkspace />; }
