'use client';
import { useEffect, useRef, useState } from 'react';
import Link from 'next/link';
import type { FeatureCollection } from 'geojson';
import { loadMapLibre, type Map as MapLibreMap } from '../maplibre-seam';
import { ORIENTATION_SOURCE_ID, orientationSource, orientationLayers } from '../kansas-orientation';
import { readBoundedJson } from '../bounded-json';
import './workspace.css';

type Product = { state: string; reason?: string; releaseId?: string; sourceId?: string; retrievedAt?: string; freshness?: string; measurementFreshness?: string; limitation?: string; sourceUrl?: string; rightsUrl?: string; evidenceRole?: string; approvalExpiresAt?: string; payloadSha256?: string; data?: FeatureCollection };
const reasons: Record<string, string> = { PIPELINE_NOT_CONFIGURED: 'Published snapshots are not configured yet.', NO_APPROVED_RELEASE: 'No approved snapshot is available.', RELEASE_STORE_UNAVAILABLE: 'Published data is temporarily unavailable.', APPROVAL_INVALID: 'This snapshot is awaiting a current approval.', APPROVAL_REVOKED: 'This snapshot has been withheld following review.' };
export default function CuratedWorkspace() {
  const [source, setSource] = useState('usgs-streamflow');
  const [product, setProduct] = useState<Product | null>(null);
  const [loading, setLoading] = useState(false);
  const [selected, setSelected] = useState<string | null>(null);
  const [attempt, setAttempt] = useState(0);
  const [release, setRelease] = useState('');
  const [history, setHistory] = useState<{ releaseId: string; publishedAt: string }[]>([]);
  const [mapState, setMapState] = useState('Map not started');
  const container = useRef<HTMLDivElement>(null), map = useRef<MapLibreMap | null>(null);
  const [ready, setReady] = useState(false);
  useEffect(() => {
    const abort = new AbortController(); const timer = setTimeout(() => abort.abort(), 15000);
    let current = true;
    queueMicrotask(() => { if (current) { setLoading(true); setProduct(null); setSelected(null); } });
    void fetch('/api/curated/' + source + (release ? '?release=' + encodeURIComponent(release) : ''), { cache: 'no-store', signal: abort.signal })
      .then(async response => { const data = await readBoundedJson(response, 8 * 1024 * 1024 + 65536, abort.signal) as Product;
        if (!data || typeof data.state !== 'string' || (data.data && (data.data.type !== 'FeatureCollection' || !Array.isArray(data.data.features) || data.evidenceRole !== 'EXTERNAL_CONTEXT_ONLY' || data.sourceId !== source))) throw new Error();
        if (current) setProduct(data); })
      .catch(() => { if (current) setProduct({ state: 'unavailable', reason: 'Request failed. Retry to check the published release.' }); })
      .finally(() => { clearTimeout(timer); if (current) setLoading(false); });
    return () => { current = false; clearTimeout(timer); abort.abort(); };
  }, [source, release, attempt]);
  useEffect(() => {
    const controller = new AbortController(); const timeout = setTimeout(() => controller.abort(), 15000);
    void fetch('/api/curated/' + source + '/history', { cache: 'no-store', signal: controller.signal })
      .then(r => readBoundedJson(r, 65536, controller.signal)).then(value => {
        const items = (value as { items?: unknown }).items;
        if (!controller.signal.aborted && Array.isArray(items)) setHistory(items.filter((v): v is { releaseId: string; publishedAt: string } => typeof v?.releaseId === 'string' && /^[a-f0-9]{64}$/.test(v.releaseId) && typeof v.publishedAt === 'string').slice(0, 20));
      }).catch(() => {}).finally(() => clearTimeout(timeout));
    return () => { clearTimeout(timeout); controller.abort(); };
  }, [source, attempt]);
  useEffect(() => {
    const interval = setInterval(() => { if (document.visibilityState === 'visible') setAttempt(v => v + 1); }, 60000);
    return () => clearInterval(interval);
  }, []);
  useEffect(() => {
    if (!product?.data) return;
    const expires = Date.parse(product.approvalExpiresAt ?? '');
    const timer = setTimeout(() => setProduct({ state: 'withheld', reason: 'Release approval expired. Refresh to check for an approved update.' }), Number.isFinite(expires) ? Math.max(0, Math.min(expires - Date.now(), 2147483647)) : 0);
    return () => clearTimeout(timer);
  }, [product]);
  useEffect(() => {
    let disposed = false; let instance: MapLibreMap | null = null;
    void loadMapLibre().then(runtime => {
      if (disposed || !container.current) return;
      runtime.setWorkerUrl('/maplibre/maplibre-gl-worker.mjs'); runtime.setWorkerCount(1);
      instance = new runtime.Map({ container: container.current, center: [-98.4, 38.6], zoom: 5.5,
        style: { version: 8, sources: { [ORIENTATION_SOURCE_ID]: orientationSource() }, layers: [
          { id: 'background', type: 'background', paint: { 'background-color': '#101e2b' } },
          ...orientationLayers({ land: '#1b3540', outline: '#83a5aa', muted: '#456c7e', graticule: '#294350' })] } });
      map.current = instance;
      instance.on('load', () => { if (!disposed) { setReady(true); setMapState('Map ready'); } });
      instance.addControl(new runtime.NavigationControl());
      instance.on('error', () => { if (!disposed) setMapState('Some map content could not be drawn. Records remain available below.'); });
    }).catch(() => { if (!disposed) setMapState('Map unavailable. Records remain available below.'); });
    return () => { disposed = true; map.current = null; instance?.remove(); };
  }, []);
  useEffect(() => {
    const instance = map.current; if (!instance || !ready) return;
    for (const id of ['curated-points','curated-outline','curated-areas']) if (instance.getLayer(id)) instance.removeLayer(id);
    if (instance.getSource('curated')) instance.removeSource('curated');
    if (!product?.data || product.sourceId !== source) return;
    // Expired alert geometry is removed from the active display; historical records stay labeled.
    const data: FeatureCollection = { ...product.data, features: product.data.features.filter(f => f.properties?.expired !== true) };
    instance.addSource('curated', { type: 'geojson', data });
    instance.addLayer({ id: 'curated-areas', type: 'fill', source: 'curated', filter: ['==','$type','Polygon'], paint: { 'fill-color': '#e3b26e', 'fill-opacity': 0.25 } });
    instance.addLayer({ id: 'curated-outline', type: 'line', source: 'curated', filter: ['==','$type','Polygon'], paint: { 'line-color': '#e3b26e', 'line-width': 2 } });
    instance.addLayer({ id: 'curated-points', type: 'circle', source: 'curated', filter: ['==','$type','Point'], paint: { 'circle-color': '#7bdcc8', 'circle-radius': 6, 'circle-stroke-color': '#102830', 'circle-stroke-width': 1 } });
    const clicked = (event: { features?: { id?: string | number }[] }) => { const id = event.features?.[0]?.id; if (id !== undefined) setSelected(String(id)); };
    instance.on('click', 'curated-points', clicked); instance.on('click', 'curated-areas', clicked);
    return () => { instance.off('click', 'curated-points', clicked); instance.off('click', 'curated-areas', clicked); };
  }, [product, source, ready]);
  const features = product?.sourceId === source ? product.data?.features ?? [] : [];
  const feature = features.find(f => String(f.id) === selected);
  return <main className="curated-workspace">
    <Link href="/">← Kansas Frontier Matrix</Link>
    <h1>Curated source snapshots</h1>
    <p>Dated provider context prepared by KFM. These snapshots are not admitted evidence or an emergency notification service.</p>
    <div className="curated-toolbar"><label>Source <select value={source} onChange={e => { setSource(e.target.value); setRelease(''); setHistory([]); }}><option value="usgs-streamflow">USGS streamflow</option><option value="nws-alerts">NWS Kansas alerts</option></select></label>
      <label>Snapshot <select value={release} onChange={e => setRelease(e.target.value)}><option value="">Latest approved</option>{history.map(h => <option key={h.releaseId} value={h.releaseId}>{h.publishedAt}</option>)}</select></label>
      <button type="button" disabled={loading} onClick={() => setAttempt(v => v + 1)}>{loading ? 'Checking…' : 'Refresh'}</button></div>
    <p role="status">{loading ? 'Checking published data…' : `${product?.state ?? 'Not checked'}${product?.freshness ? ' · snapshot retrieval: ' + product.freshness : ''}`}</p>
    {product?.data && source === 'usgs-streamflow' && <p>Measurement freshness: {product.measurementFreshness ?? 'unknown'}. Retrieval time does not change observation dates.</p>}
    {product?.reason && <p>{reasons[product.reason] ?? (product.reason.includes(' ') ? product.reason : 'Published data is unavailable. Refresh to check again.')}</p>}
    {product?.retrievedAt && <p>Retrieved <time dateTime={product.retrievedAt}>{product.retrievedAt}</time> · {features.length} records</p>}
    <div ref={container} className="curated-map" role="region" aria-label="Dated Kansas provider context map" />
    <p>{mapState} · The Census Kansas boundary is display context only. Records without provider geometry are listed below.</p>
    {product?.releaseId && <p><a href={'/api/curated/' + source + '?release=' + product.releaseId + '&download=1'} download={source + '-' + product.releaseId + '.json'}>Download this snapshot with provenance</a><br /><small>SHA-256: {product.payloadSha256}</small></p>}
    {product?.sourceUrl && <p><a href={product.sourceUrl}>Provider query</a>{' · '}<a href={product.rightsUrl}>Provider terms</a></p>}
    {product?.limitation && <p>{product.limitation}</p>}
    {feature && <section aria-label="Selected source record"><h2>Selected record</h2><dl>{Object.entries(feature.properties ?? {}).map(([key, value]) => <div key={key}><dt>{key}</dt><dd>{value === null ? 'Missing' : typeof value === 'object' ? JSON.stringify(value) : String(value)}</dd></div>)}</dl></section>}
    <h2>Source records</h2>
    <ul className="curated-records">{features.map(f => <li key={String(f.id)}><button type="button" aria-pressed={selected === String(f.id)} onClick={() => setSelected(String(f.id))}>{String(f.properties?.headline ?? f.properties?.stationId ?? f.id)}{f.properties?.expired ? ' · expired' : ''}</button><small>{String(f.properties?.observedAt ?? '')}{' '}{f.properties?.value === null ? 'Missing value' : f.properties?.value !== undefined ? String(f.properties.value) + ' ' + String(f.properties.unit ?? 'unit unavailable') : ''}</small></li>)}</ul>
  </main>;
}
