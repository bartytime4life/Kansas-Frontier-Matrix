"use client";
import { useEffect, useRef, useState } from 'react';
import type { Map as MapLibreMap } from '../maplibre-seam';
import { DEMO_SCENARIOS } from '../../scripts/welcome-demos/scenarios.mjs';
import { capturePixelRatio, nativeCaptureReady, captureCameraAt, jpegDataUrlBytes } from '../../scripts/welcome-demos/capture-metrics.mjs';

export type DemoScenario = typeof DEMO_SCENARIOS[number];
export type DemoEvidence = { ready: boolean; pending?: string; error?: string; sourceTimes: string[]; attribution: string[] };
type Props = {
  getMap: () => MapLibreMap | null;
  setCapturePixelRatio: (ratio: number | null) => void;
  beforeFrame: (scenario: DemoScenario, elapsedMs: number) => void;
  prepareBenchmark: () => void;
  freezeSourceFrame: (scenario: DemoScenario) => void;
  releaseSourceFrame: () => void;
  captureLayerStates: (scenario: DemoScenario) => unknown[];
  prepare: (scenario: DemoScenario) => void;
  evidence: (scenario: DemoScenario) => DemoEvidence;
  extraCanvases: () => (HTMLCanvasElement | null)[];
  finish: () => void;
};
const OUTPUT_WIDTH = 1280, OUTPUT_HEIGHT = 720;
const aborted = () => new DOMException('Recording cancelled', 'AbortError');
function delay(milliseconds: number, signal: AbortSignal) {
  return new Promise<void>((resolve, reject) => {
    if (signal.aborted) { reject(aborted()); return; }
    const cancel = () => { clearTimeout(timer); reject(aborted()); };
    const timer = window.setTimeout(() => { signal.removeEventListener('abort', cancel); resolve(); }, milliseconds);
    signal.addEventListener('abort', cancel, { once: true });
  });
}
async function settleMapSize(map: MapLibreMap, signal: AbortSignal, setRatio: (ratio: number) => void) {
  await delay(50, signal);
  const host = map.getContainer();
  setRatio(capturePixelRatio(host.clientWidth, host.clientHeight)); map.resize();
  await delay(100, signal);
}

async function save(id: string, extension: string, blob: Blob, signal: AbortSignal) {
  const response = await fetch(`/__welcome-demo-capture/${id}.${extension}`, { method: 'POST', body: blob, signal, credentials: 'omit' });
  if (!response.ok) throw new Error(`Local capture save failed (${response.status})`);
}
function plain(text: string) { return text.replace(/<[^>]*>/g, '').replace(/&copy;/g, '©').replace(/&amp;/g, '&'); }
function wrap(context: CanvasRenderingContext2D, value: string, x: number, y: number, width: number, lineHeight: number, maxLines = 2) {
  const words = value.split(/\s+/); let line = '', row = 0;
  for (const word of words) {
    if (context.measureText(`${line} ${word}`).width > width && line) {
      context.fillText(line, x, y + row * lineHeight); line = word; row++;
      if (row >= maxLines) return;
    } else line += `${line ? ' ' : ''}${word}`;
  }
  if (row < maxLines) context.fillText(line, x, y + row * lineHeight);
}
/** Actual map canvas capture; imported only in an explicitly opted-in local Vite session. */
export default function DevWelcomeRecorder(props: Props) {
  const latest = useRef(props), controller = useRef<AbortController | null>(null), restoreViewport = useRef<(() => void) | null>(null);
  const [status, setStatus] = useState('Ready. Generate records the actual map; unavailable sources fail visibly.'), [active, setActive] = useState(false);
  const [selected, setSelected] = useState(DEMO_SCENARIOS[0].id), [results, setResults] = useState<Record<string, string>>({});
  useEffect(() => { latest.current = props; }, [props]);
  useEffect(() => () => { controller.current?.abort(); restoreViewport.current?.(); restoreViewport.current = null; latest.current.setCapturePixelRatio(null); latest.current.finish(); }, []);

  const renderTour = async (scenario: DemoScenario, signal: AbortSignal, previewOnly = false) => {
    setStatus(`${scenario.id}: preparing actual map sources`);
    latest.current.prepare(scenario);
    await delay(150, signal);
    const map = latest.current.getMap();
    if (!map) throw new Error('Production map is not ready');
    await settleMapSize(map, signal, latest.current.setCapturePixelRatio);
    const camera = (fraction: number) => {
      const value = captureCameraAt(scenario.start, scenario.end, fraction);
      return { ...value, center: [...value.center] as [number, number] };
    };
    const waitReady = async (timeout: number, phase: string): Promise<DemoEvidence> => {
      const started = performance.now();
      while (!signal.aborted) {
        const evidence = latest.current.evidence(scenario);
        if (evidence.error) throw new Error(evidence.error);
        if (evidence.ready) return evidence;
        if (performance.now() - started > timeout) throw new Error(`${phase}: ${evidence.pending ?? 'actual source tiles'} did not become ready`);
        setStatus(`${scenario.id}: ${phase} · ${evidence.pending ?? 'source tiles'}`);
        if (map.getStyle()?.layers?.length) map.redraw();
        await delay(100, signal);
      }
      throw aborted();
    };
    const previousRepaint = map.repaint;
    map.stop(); map.repaint = false;
    const capturedAt = new Date().toISOString();
    try {
      // Populate the actual tile cache across the tour before exporting frames.
      for (const fraction of previewOnly ? [0] : [0, .5, 1, 0]) {
        map.jumpTo(camera(fraction));
        if (map.getStyle()?.layers?.length) map.redraw();
        await delay(30, signal);
        await waitReady(60_000, 'warming the tour viewport');
      }
      const evidence = await waitReady(10_000, 'confirming source clocks');
      latest.current.freezeSourceFrame(scenario);
      const source = map.getCanvas();
      if (!nativeCaptureReady(source)) throw new Error(`Insufficient native HD map pixels: ${source.width}×${source.height}`);
      const canvas = document.createElement('canvas'); canvas.width = OUTPUT_WIDTH; canvas.height = OUTPUT_HEIGHT;
      const context = canvas.getContext('2d', { alpha: false });
      if (!context) throw new Error('Frame export canvas unavailable');
      const labelCanvas = document.createElement('canvas'); labelCanvas.width = OUTPUT_WIDTH; labelCanvas.height = OUTPUT_HEIGHT;
      const labels = labelCanvas.getContext('2d')!;
      const top = labels.createLinearGradient(0, 0, 0, 185); top.addColorStop(0, '#03131fec'); top.addColorStop(1, '#03131f00');
      labels.fillStyle = top; labels.fillRect(0, 0, OUTPUT_WIDTH, 190);
      labels.fillStyle = '#efd18d'; labels.font = '600 11px sans-serif'; labels.fillText('KANSAS FRONTIER MATRIX  /  RENDERED MAP TOUR', 34, 33);
      labels.fillStyle = '#f3f7f6'; labels.font = '600 31px sans-serif'; labels.fillText(scenario.title, 34, 76);
      labels.font = '17px sans-serif'; labels.fillStyle = '#d8e8ed'; wrap(labels, scenario.caption, 35, 107, OUTPUT_WIDTH - 70, 23);
      const bottom = labels.createLinearGradient(0, 540, 0, OUTPUT_HEIGHT); bottom.addColorStop(0, '#03131f00'); bottom.addColorStop(.38, '#03131fd9'); bottom.addColorStop(1, '#03131ff5');
      labels.fillStyle = bottom; labels.fillRect(0, 540, OUTPUT_WIDTH, OUTPUT_HEIGHT - 540);
      labels.font = '13px sans-serif'; labels.fillStyle = '#e3c683'; wrap(labels, evidence.sourceTimes.join(' · '), 34, 599, OUTPUT_WIDTH - 68, 17, 2);
      labels.fillStyle = '#cee0e6'; labels.font = '12px sans-serif'; wrap(labels, scenario.limitation, 34, 638, OUTPUT_WIDTH - 68, 17, 2);
      labels.fillStyle = '#9bb9c5'; labels.font = '11px sans-serif'; wrap(labels, `${[...new Set(evidence.attribution.map(plain))].join(' · ')}  |  Rendered ${capturedAt.slice(0, 10)}`, 34, 689, OUTPUT_WIDTH - 68, 14, 2);
      const outputId = `${scenario.id}${previewOnly ? '.preview' : ''}`;
      const totalFrames = previewOnly ? 1 : 120;
      const metadata = { ...scenario, previewOnly, capturedLayerStates: [] as unknown[], kind: 'rendered-software-tour', state: 'rendering', quality: 'incomplete', capturedAt, sourceTimes: evidence.sourceTimes, attribution: evidence.attribution, width: OUTPUT_WIDTH, height: OUTPUT_HEIGHT, nativeMapViewport: { width: source.clientWidth, height: source.clientHeight, pixelWidth: source.width, pixelHeight: source.height, pixelRatio: map.getPixelRatio(), verificationMethod: 'measured-runtime-before-frame-export' }, frameCount: 0, playbackFps: 24, durationSeconds: previewOnly ? 0 : 5, captureWallSeconds: 0, sourceClocks: 'Actual pinned source frame; no source value interpolation', captureMethod: '120 actual production MapLibre redraws, each source-ready pose exported to JPEG', annotations: 'burned-in', cameraMethod: 'Public MapLibre jumpTo/redraw; camera-only interpolation', frameBytes: [] as number[], frameTimings: [] as Record<string, number>[] };
      await save(outputId, 'json', new Blob([JSON.stringify(metadata, null, 2)], { type: 'application/json' }), signal);
      const started = performance.now();
      for (let index = 0; index < totalFrames; index++) {
        if (signal.aborted) throw aborted();
        const frameStarted = performance.now();
        const phases: Record<string, number> = { frame: index };
        map.jumpTo(camera(index / 119));
        const blob = await new Promise<Blob>((resolve, reject) => {
          let settled = false, retryTimer = 0, nativeRedrawStarted = 0;
          const cleanup = () => { map.off('render', render); signal.removeEventListener('abort', cancel); clearTimeout(timer); clearTimeout(retryTimer); };
          const done = (value?: Blob | null, error?: Error) => { if (settled) return; settled = true; cleanup(); if (error || !value) reject(error ?? new Error('Empty native frame')); else resolve(value); };
          const cancel = () => done(null, aborted());
          const attempt = () => {
            if (settled) return;
            if (signal.aborted) { cancel(); return; }
            try {
              latest.current.beforeFrame(scenario, index * 1000 / 24);
              map.once('render', render);
              nativeRedrawStarted = performance.now(); map.redraw();
            } catch (error) { done(null, error instanceof Error ? error : new Error('Actual map redraw failed')); }
          };
          const render = () => {
            try {
              // Source checks run AFTER this pose has rendered and updated its
              // actual tile cache. Export that very frame if ready; retry only
              // pending sources, with no unconditional timer or second render.
              const actual = latest.current.evidence(scenario);
              if (actual.error) { done(null, new Error(actual.error)); return; }
              if (!actual.ready) {
                if (performance.now() - frameStarted >= 10_000) { done(null, new Error(`Frame ${index + 1}: ${actual.pending ?? 'source tiles'} not ready`)); return; }
                setStatus(`${scenario.id}: checking frame ${index + 1}/${totalFrames} · ${actual.pending ?? 'source tiles'}`);
                retryTimer = window.setTimeout(attempt, 50); return;
              }
              const pixelsStarted = performance.now();
              phases.sourceReadyMs = pixelsStarted - frameStarted;
              phases.nativeRedrawMs = pixelsStarted - nativeRedrawStarted;
              const scale = Math.max(OUTPUT_WIDTH / source.width, OUTPUT_HEIGHT / source.height);
              const width = source.width * scale, height = source.height * scale;
              if (scale > 1.00001) throw new Error('Frame export would enlarge native pixels');
              context.drawImage(source, (OUTPUT_WIDTH - width) / 2, (OUTPUT_HEIGHT - height) / 2, width, height);
              if (scenario.sources.includes('nws-forecast-wind')) {
                const wind = latest.current.extraCanvases()[0];
                if (!wind?.width || !wind.height) throw new Error('Actual forecast wind canvas unavailable');
                context.drawImage(wind, (OUTPUT_WIDTH - width) / 2, (OUTPUT_HEIGHT - height) / 2, width, height);
              }
              context.drawImage(labelCanvas, 0, 0);
              phases.nativeDrawMs = performance.now() - pixelsStarted;
              const encodeStarted = performance.now();
              const bytes = jpegDataUrlBytes(canvas.toDataURL('image/jpeg', .9));
              phases.jpegEncodeMs = performance.now() - encodeStarted;
              done(new Blob([bytes], { type: 'image/jpeg' }));
            } catch (error) { done(null, error instanceof Error ? error : new Error('Actual map frame export failed')); }
          };
          const timer = window.setTimeout(() => done(null, new Error('Actual map frame export timed out')), 20_000);
          signal.addEventListener('abort', cancel, { once: true });
          attempt();
        });
        const uploadStarted = performance.now();
        await save(previewOnly ? outputId : `${scenario.id}.frame-${String(index).padStart(3, '0')}`, 'jpg', blob, signal);
        phases.uploadMs = performance.now() - uploadStarted; phases.frameWallMs = performance.now() - frameStarted;
        if (index < 3) metadata.frameTimings.push(phases);
        metadata.capturedLayerStates = latest.current.captureLayerStates(scenario);
        metadata.frameBytes.push(blob.size);
        metadata.frameCount = index + 1;
        setStatus(`${scenario.id}: rendered ${index + 1}/${totalFrames} real map frames · ${((performance.now() - started) / 1000).toFixed(1)}s wall time · ready ${phases.sourceReadyMs.toFixed(0)}ms / draw ${phases.nativeDrawMs.toFixed(0)}ms / JPEG ${phases.jpegEncodeMs.toFixed(0)}ms / upload ${phases.uploadMs.toFixed(0)}ms`);
        if (index === 2 && !previewOnly) await save(outputId, 'json', new Blob([JSON.stringify(metadata, null, 2)], { type: 'application/json' }), signal);
      }
      await waitReady(10_000, 'confirming final source frame');
      metadata.captureWallSeconds = (performance.now() - started) / 1000;
      metadata.state = previewOnly ? 'preview' : 'complete'; metadata.quality = previewOnly ? 'preview-review-required' : 'rendered-review-required';
      await save(outputId, 'json', new Blob([JSON.stringify(metadata, null, 2)], { type: 'application/json' }), signal);
      const overlay = await new Promise<Blob | null>(resolve => labelCanvas.toBlob(resolve, 'image/png'));
      if (overlay && !previewOnly) await save(scenario.id, 'png', overlay, signal);
    } finally { map.repaint = previousRepaint; map.stop(); latest.current.releaseSourceFrame(); }
  };

  const generate = async (all: boolean, previewOnly = false, fromSelected = false) => {
    if (controller.current) return;
    const cancellation = new AbortController(); controller.current = cancellation; setActive(true);
    const map = latest.current.getMap();
    if (map) {
      const host = map.getContainer(), previousStyle = host.getAttribute('style');
      restoreViewport.current = () => { if (previousStyle === null) host.removeAttribute('style'); else host.setAttribute('style', previousStyle); map.resize(); };
      host.style.width = `${OUTPUT_WIDTH}px`; host.style.height = `${OUTPUT_HEIGHT}px`;
      host.style.maxWidth = 'none'; host.style.maxHeight = 'none';
      latest.current.setCapturePixelRatio(1); map.resize();
    }
    const scenarios = all ? fromSelected ? DEMO_SCENARIOS.slice(Math.max(0, DEMO_SCENARIOS.findIndex(scene => scene.id === selected))) : DEMO_SCENARIOS : DEMO_SCENARIOS.filter(scene => scene.id === selected);
    try {
      for (const scenario of scenarios) {
        if (cancellation.signal.aborted) break;
        try { await renderTour(scenario, cancellation.signal, previewOnly); setResults(old => ({ ...old, [scenario.id]: previewOnly ? 'Source preview + actual layer-state JSON saved' : '120 actual frames saved; awaiting video encoding' })); }
        catch (error) {
          const message = error instanceof Error ? error.message : 'Recording failed';
          setResults(old => ({ ...old, [scenario.id]: message }));
          if (cancellation.signal.aborted) break;
        }
      }
      setStatus(cancellation.signal.aborted ? 'Cancelled. Completed local captures remain saved.' : 'Finished. Complete source-ready JPEG sequences are in /tmp/kfm-welcome-demo-recordings. Encode only complete 120-frame tours.');
    } finally { restoreViewport.current?.(); restoreViewport.current = null; latest.current.setCapturePixelRatio(null); latest.current.finish(); controller.current = null; setActive(false); }
  };
  const benchmark = () => {
    if (controller.current) return;
    const cancellation = new AbortController(); controller.current = cancellation; setActive(true);
    latest.current.prepareBenchmark();
    let timerTicks = 0, animationFrames = 0, timer = 0, frame = 0, stopTimer = 0, lastStatus = 0;
    const started = performance.now();
    const finish = () => {
      clearTimeout(timer); clearTimeout(stopTimer); window.cancelAnimationFrame(frame);
      cancellation.signal.removeEventListener('abort', finish);
      const seconds = (performance.now() - started) / 1000;
      setStatus(`Clock benchmark ${cancellation.signal.aborted ? 'cancelled' : 'finished'}: timer33ms ${timerTicks} ticks (${(timerTicks / seconds).toFixed(2)}/s); rAF ${animationFrames} frames (${(animationFrames / seconds).toFixed(2)}/s); elapsed ${seconds.toFixed(3)}s. No map calls or canvas copies.`);
      controller.current = null; setActive(false);
    };
    const tick = () => {
      timerTicks++;
      const now = performance.now();
      if (now - lastStatus >= 1000) { lastStatus = now; setStatus(`Clock benchmark ${(now - started).toFixed(0)}ms: timer33ms ${timerTicks} ticks; rAF ${animationFrames} frames. No map calls or canvas copies.`); }
      timer = window.setTimeout(tick, 33);
    };
    const animate = () => { animationFrames++; frame = window.requestAnimationFrame(animate); };
    cancellation.signal.addEventListener('abort', finish, { once: true });
    setStatus('Measuring browser clocks for 10 seconds. No map calls or canvas copies.');
    timer = window.setTimeout(tick, 33); frame = window.requestAnimationFrame(animate); stopTimer = window.setTimeout(finish, 10_000);
  };
  return <aside aria-label="Local map demo recorder" style={{ position: 'fixed', zIndex: 100000, right: 18, top: 100, width: 370, maxHeight: '70vh', overflow: 'auto', background: '#061e2ef5', color: '#e5f0f4', padding: 20, border: '1px solid #a88b51', borderRadius: 12, boxShadow: '0 15px 60px #0008', font: '13px/1.5 sans-serif' }}>
    <p style={{ color: '#e1bc6a', margin: 0, fontSize: 10, letterSpacing: '.15em' }}>LOCAL CAPTURE WORKBENCH · 1280 × 720</p>
    <h2 style={{ margin: '5px 0 12px', fontSize: 22 }}>Record the real map.</h2>
    <p role="status" aria-live="polite">{status}</p>
    <label>Scenario<select aria-label="Demo recording scenario" value={selected} disabled={active} onChange={event => setSelected(event.target.value)} style={{ width: '100%', padding: 8, margin: '6px 0 12px', color: '#132635', background: '#eff5f3' }}>{DEMO_SCENARIOS.map(scene => <option key={scene.id} value={scene.id}>{scene.id} · {scene.title}</option>)}</select></label>
    <div style={{ display: 'flex', gap: 8, flexWrap: 'wrap' }}><button disabled={active} onClick={() => void generate(true)}>Render all 16 map tours</button><button disabled={active} onClick={() => void generate(true, false, true)}>Render from selected onward</button><button disabled={active} onClick={() => void generate(false)}>Render selected map tour</button><button disabled={active} onClick={() => void generate(false, true)}>Export source preview</button><button disabled={!active} onClick={() => controller.current?.abort()}>Cancel rendering</button><button disabled={active} onClick={benchmark}>Measure 10s browser clocks</button></div>
    {Object.keys(results).length > 0 && <ul aria-label="Recording results">{Object.entries(results).map(([id, value]) => <li key={id}><strong>{id}</strong>: {value}</li>)}</ul>}
    <small>Captures contain map pixels and public source labels only. Unavailable source data is never manufactured. Leave this tab visible.</small>
  </aside>;
}
