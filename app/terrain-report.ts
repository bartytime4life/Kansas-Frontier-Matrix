import { TRANSECT_LIMITS, TRANSECT_METHOD, transectGeometry, type TerrainTransect } from './terrain-transect';
export type TerrainReportContext = {
    version: 1;
    capturedAt: string;
    pendingTiles: number;
    profile: TerrainTransect;
};
const object = (v: unknown): v is Record<string, unknown> => !!v && typeof v === 'object' && !Array.isArray(v);
const keys = (v: Record<string, unknown>, allowed: string[]) => Object.keys(v).length === allowed.length && allowed.every(k => Object.hasOwn(v, k));
const number = (v: unknown): v is number => typeof v === 'number' && Number.isFinite(v);
const integer = (v: unknown): v is number => number(v) && Number.isInteger(v) && v >= 0;
const text = (v: unknown): v is string => typeof v === 'string' && v.length <= 4000;
const coordinate = (v: unknown): v is [
    number,
    number
] => Array.isArray(v) && v.length === 2 && v.every(number) && Math.abs(v[0]) <= 180 && Math.abs(v[1]) <= 85;
export function validTerrainReport(v: unknown): v is TerrainReportContext {
    if (!object(v) || !keys(v, ['version', 'capturedAt', 'pendingTiles', 'profile']) || v.version !== 1 || !text(v.capturedAt) || !Number.isFinite(Date.parse(v.capturedAt)) || !integer(v.pendingTiles) || v.pendingTiles > 24 || !object(v.profile))
        return false;
    const p = v.profile;
    if (!keys(p, ['line', 'mode', 'length', 'stations', 'sources', 'supported', 'error']) || !['ground', 'surface', 'canopy'].includes(String(p.mode)) || p.error !== null || !number(p.length) || p.length <= 0 || !Array.isArray(p.line) || p.line.length < 2 || p.line.length > TRANSECT_LIMITS.vertices || !p.line.every(coordinate) || !Array.isArray(p.stations) || !p.stations.length || p.stations.length > TRANSECT_LIMITS.stations || !Array.isArray(p.sources) || !p.sources.length || p.sources.length > TRANSECT_LIMITS.tiles || !integer(p.supported) || !p.supported)
        return false;
    const sources = new Map<string, string>();
    for (const s of p.sources) {
        if (!object(s) || !keys(s, ['tile', 'requestKey', 'source', 'verticalReference', 'acquisition', 'horizontalCrs', 'spacing', 'spacingUnits', 'hashes', 'cacheTime', 'stale']) || !['tile', 'requestKey', 'source', 'verticalReference', 'acquisition', 'horizontalCrs', 'spacingUnits'].every(k => text(s[k])) || !s.tile || sources.has(String(s.tile)) || !Array.isArray(s.spacing) || s.spacing.length !== 2 || !s.spacing.every(n => number(n) && n > 0) || !Array.isArray(s.hashes) || s.hashes.length > 256 || !s.hashes.every(h => typeof h === 'string' && /^(?:sha256:)?[a-f0-9]{64}$/.test(h)) || s.cacheTime !== null && (!text(s.cacheTime) || !Number.isFinite(Date.parse(s.cacheTime))) || typeof s.stale !== 'boolean')
            return false;
        sources.set(String(s.tile), String(s.requestKey));
    }
    let previous = -1, supported = 0;
    for (const s of p.stations) {
        if (!object(s) || !keys(s, ['distance', 'coordinate', 'value', 'tile', 'requestKey', 'index', 'row', 'column', 'center']) || !number(s.distance) || s.distance < previous || s.distance > p.length || !coordinate(s.coordinate) || s.value !== null && !number(s.value))
            return false;
        previous = s.distance;
        if (s.value !== null) {
            supported++;
            if (p.mode === 'canopy' && (s.value as number) < 0)
                return false;
        }
        if (s.tile === null) {
            if (s.value !== null || [s.requestKey, s.index, s.row, s.column, s.center].some(n => n !== null))
                return false;
        }
        else if (!text(s.tile) || !sources.has(s.tile) || sources.get(s.tile) !== s.requestKey || !integer(s.index) || !integer(s.row) || s.row < 1 || !integer(s.column) || s.column < 1 || !coordinate(s.center))
            return false;
    }
    return p.stations[0].distance === 0 && previous === p.length && supported === p.supported && JSON.stringify(v).length <= 768000;
}
export function captureTerrainReport(profile: TerrainTransect, pendingTiles: number, redacted: boolean, capturedAt = new Date().toISOString()): TerrainReportContext | undefined {
    if (redacted)
        return undefined;
    const value = { version: 1, capturedAt, pendingTiles, profile };
    return validTerrainReport(value) ? JSON.parse(JSON.stringify(value)) as TerrainReportContext : undefined;
}
export const terrainQuantity = (c: TerrainReportContext) => ({ ground: 'Ground', surface: 'Surface', canopy: 'Canopy height' }[c.profile.mode]);
export function terrainReportSummary(c: TerrainReportContext) { const p = c.profile; return `${terrainQuantity(c)} profile · ${(p.length / 1000).toFixed(3)} km approximate line · ${p.supported}/${p.stations.length} supported stations · ${p.sources.length} source tiles. Captured ${c.capturedAt}.${c.pendingTiles ? ` ${c.pendingTiles} tiles were still arriving; this is a partial snapshot.` : ''}`; }
export function terrainReportMarkdown(c: TerrainReportContext) { return ['## Captured terrain cross-section · external source context', terrainReportSummary(c), 'Heights are unscaled source metres. Station counts are not area coverage. The captured profile stays fixed as the map changes.', ...c.profile.sources.map(s => `Source tile: ${s.tile} | ${s.source}\nVertical reference: ${s.verticalReference}\nAcquisition: ${s.acquisition}\nHorizontal CRS: ${s.horizontalCrs}; grid spacing: ${s.spacing.join(' × ')} ${s.spacingUnits}\nArtifact cache: ${s.cacheTime ?? 'not supplied'}${s.stale ? ' (stale)' : ''}\nRequest: ${s.requestKey}\nSource SHA-256: ${s.hashes.join(', ') || 'not supplied'}`), TRANSECT_METHOD, 'All station values, gaps and source-cell indices are retained in report JSON and the station CSV.'].join('\n\n'); }
const escape = (v: unknown) => String(v ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]!));
export function terrainReportMarkup(c: TerrainReportContext) {
    const p = c.profile, g = transectGeometry(p), e = escape;
    const svg = `<svg viewBox="0 0 320 150" role="img" aria-label="${e(terrainQuantity(c))} source cross-section; gaps and source boundaries are retained"><rect width="320" height="150" fill="#f0f6f6"/><path d="M12 12V124H308" stroke="#91a7ae" fill="none"/>${g.paths.map(d => `<path d="${d}" stroke="#147c86" fill="none" stroke-width="1"/>`).join('')}${g.points.map(q => q ? `<circle cx="${q.x}" cy="${q.y}" r="1.25" fill="#147c86"/>` : '').join('')}<g font-size="8" fill="#294f60"><text x="12" y="144">A · 0 m</text><text x="308" y="144" text-anchor="end">B · ${p.length.toFixed(1)} m</text></g></svg>`;
    return `<section class="sr-card"><h2>${e(terrainQuantity(c))} · captured terrain cross-section</h2><p>${e(terrainReportSummary(c))}</p><figure class="sr-map">${svg}<figcaption>${g.low.toFixed(3)}–${g.high.toFixed(3)} unscaled source metres · ${p.mode === 'canopy' ? 'height above supported same-survey ground' : 'vertical reference may differ by tile'}. Guides split at unsupported stations and source boundaries. Heights are not display-exaggerated; graph axes scale independently.</figcaption></figure><p class="sr-caution">${e(TRANSECT_METHOD)}</p><h3>Source tiles & acquisition</h3>${p.sources.map(s => `<article class="sr-source"><strong>${e(s.source)}</strong><dl class="sr-meta"><div><dt>Tile</dt><dd>${e(s.tile)}</dd></div><div><dt>Acquisition</dt><dd>${e(s.acquisition)}</dd></div><div><dt>Vertical reference</dt><dd>${e(s.verticalReference)}</dd></div><div><dt>Horizontal CRS / spacing</dt><dd>${e(s.horizontalCrs)} · ${s.spacing.map(n => n.toFixed(3)).join(' × ')} ${e(s.spacingUnits)}</dd></div><div><dt>Artifact cache</dt><dd>${e(s.cacheTime ?? 'Not supplied')}${s.stale ? ' · stale' : ''}</dd></div></dl><p>Request: ${e(s.requestKey)}</p><details><summary>Source hashes</summary><p>${s.hashes.map(e).join('<br/>') || 'Not supplied'}</p></details></article>`).join('')}<details><summary>All ${p.stations.length} profile stations</summary><div class="sr-table-wrap"><table><thead><tr><th>Station</th><th>Distance ≈ m</th><th>Source m</th><th>Tile / row / column</th></tr></thead><tbody>${p.stations.map((s, i) => `<tr><td>${i + 1}</td><td>${s.distance.toFixed(2)}</td><td>${s.value === null ? 'Not supported' : s.value.toFixed(3)}</td><td>${e(s.tile ?? 'No source tile')} · ${s.row ?? '—'} / ${s.column ?? '—'}</td></tr>`).join('')}</tbody></table></div></details></section>`;
}
export function terrainReportCSV(c: TerrainReportContext) {
    const cell = (v: unknown) => { const s = typeof v === 'number' ? String(v) : String(v ?? ''); return '"' + (typeof v === 'string' && /^[\s]*[=+@-]/.test(s) ? "'" + s : s).replaceAll('"', '""') + '"'; };
    const header = ['station', 'distance_approx_m', 'height_source_m', 'quantity', 'line_longitude', 'line_latitude', 'source_cell_longitude', 'source_cell_latitude', 'tile', 'row', 'column', 'cell_index', 'request_key', 'source', 'vertical_reference', 'acquisition', 'horizontal_crs', 'artifact_cache_time', 'stale', 'source_sha256', 'captured_at', 'pending_tiles_at_capture'];
    return [header.map(cell).join(','), ...c.profile.stations.map((s, i) => { const source = c.profile.sources.find(t => t.tile === s.tile); return [i + 1, s.distance, s.value, c.profile.mode, ...s.coordinate, ...(s.center ?? [null, null]), s.tile, s.row, s.column, s.index, s.requestKey, source?.source, source?.verticalReference, source?.acquisition, source?.horizontalCrs, source?.cacheTime, source?.stale, source?.hashes.join(';'), c.capturedAt, c.pendingTiles].map(cell).join(','); })].join('\r\n');
}
