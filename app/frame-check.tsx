"use client";
import { useEffect, useRef, useState } from "react";
import type { Map as GLMap, GeoJSONSource } from "./maplibre-seam";
import { uploadedGeoJSON } from "./map-performance";
import { waterFlowDiagnosticState } from "./water-flow-sync";
import { samePacingWorkload, type PacingRecord } from "./frame-check-model";

export function frameStatistics(intervals: readonly number[], elapsed: number) {
  const sorted = [...intervals].sort((a, b) => a - b);
  return { frames: intervals.length, fps: elapsed > 0 ? intervals.length * 1000 / elapsed : 0,
    p95Ms: sorted.length ? sorted[Math.min(sorted.length - 1, Math.floor(sorted.length * .95))] : 0,
    maxMs: sorted.at(-1) ?? 0, over25ms: intervals.filter(value => value > 25).length };
}
const digest = async (value: unknown) => [...new Uint8Array(await crypto.subtle.digest("SHA-256", new TextEncoder().encode(JSON.stringify(value))))].map(byte => byte.toString(16).padStart(2, "0")).join("");
export async function displaySignature(map: GLMap) {
  const style = map.getStyle();
  const data = Object.keys(style.sources).sort().map(id => {
    const source = map.getSource(id);
    const collection = source?.type === "geojson" ? uploadedGeoJSON(source as GeoJSONSource) : undefined;
    return [id, collection ?? style.sources[id]];
  });
  const flow = waterFlowDiagnosticState(map);
  // Custom ribbons do not live in a GeoJSON source. Include their actual
  // provider geometry/direction and gauge cues, not only their reach count.
  return digest([data, flow.cells, flow.cues]);
}
const layerIdentity = (map: GLMap) => (map.getStyle().layers ?? []).map(layer => ({
  id: layer.id, type: layer.type, source: 'source' in layer ? layer.source : null,
  sourceLayer: 'source-layer' in layer ? layer['source-layer'] : null,
  minzoom: layer.minzoom, maxzoom: layer.maxzoom,
  filter: 'filter' in layer ? layer.filter : null, layout: layer.layout,
}));
const ready = (map: GLMap, selection: Record<string, unknown>) => {
  const flow = waterFlowDiagnosticState(map);
  const sourceStates = selection.sourceStates as Record<string, string> | undefined;
  return map.isStyleLoaded() === true && map.areTilesLoaded() && !flow.samplingPending
    && Boolean(sourceStates) && Object.values(sourceStates!).every(state => ['ready','empty'].includes(state))
    && !['loading','partial','unavailable'].includes(flow.status.state);
};
async function workload(map: GLMap, selection: Record<string, unknown>) {
  const canvas = map.getCanvas(), center = map.getCenter();
  const gl = canvas.getContext('webgl2'), debug = gl?.getExtension('WEBGL_debug_renderer_info');
  const features = map.queryRenderedFeatures().map(feature => JSON.stringify({
    source: feature.source, sourceLayer: feature.sourceLayer, layer: feature.layer.id,
    id: feature.id, geometry: feature.geometry, properties: feature.properties,
  })).sort();
  const flow = waterFlowDiagnosticState(map);
  return {
    camera: [center.lng,center.lat,map.getZoom(),map.getBearing(),map.getPitch()],
    viewport: [canvas.clientWidth,canvas.clientHeight], canvas: [canvas.width,canvas.height],
    browserViewport: [window.innerWidth,window.innerHeight], devicePixelRatio: window.devicePixelRatio,
    renderer: debug ? String(gl!.getParameter(debug.UNMASKED_RENDERER_WEBGL)) : 'Unavailable',
    userAgent: navigator.userAgent, hardwareConcurrency: navigator.hardwareConcurrency,
    selection, projection: map.getProjection()?.type ?? 'mercator', terrain: map.getTerrain(),
    layerIdentity: layerIdentity(map), sourceDigest: await displaySignature(map),
    visibleFeatureDigest: await digest(features), visibleFeatures: features.length,
    flowSegments: flow.segments, durationMs: 12000, inputIntervalMs: 250,
    inputSequence: ['ArrowRight','ArrowDown','ArrowLeft','ArrowUp'],
  };
}
type Result = PacingRecord & { visibleLayers: number; selectedLayers: number; visibleDataFeatures: number; renderer: string; viewport: number[]; canvasPixels: number[]; movementEnds: number; inputDispatchMaxMs: number; url: string; recordedAt: string };
/** Explicit diagnostic only; no listeners, polling, upload, or telemetry in ordinary views. */
export function FrameCheck({ map, selectedLayers, selection = {} }: { map: GLMap | null; selectedLayers:number; selection?: Record<string, unknown> }) {
  const selectionRef = useRef(selection);
  useEffect(() => { selectionRef.current = selection; }, [selection]);
  const [running,setRunning] = useState(false), [result,setResult] = useState<Result | null>(null), [error,setError] = useState<string | null>(null);
  const [cancel,setCancel] = useState<{run:()=>void} | null>(null);
  useEffect(() => () => cancel?.run(), [cancel]);
  const measure = async (moving: boolean, interrupted = false) => {
    if (!map || running) return;
    setRunning(true); setResult(null); setError(null);
    const center=map.getCenter(), pose={center:[center.lng,center.lat] as [number,number],zoom:map.getZoom(),bearing:map.getBearing(),pitch:map.getPitch()};
    let stopped=false, finished=false, frame=0, timer:ReturnType<typeof setTimeout> | undefined, start=0, lastBrowser=0, lastMap=0, steps=0;
    let keys:ReturnType<typeof setInterval> | undefined, movementEnds=0,inputDispatchMaxMs=0,focusInterrupted=false;
    const browserIntervals:number[]=[],mapIntervals:number[]=[];
    const ended=()=>{movementEnds++;};
    const blurred=()=>{focusInterrupted=true;};
    const rendered=()=>{const now=performance.now();if(start && now>=start){if(lastMap)mapIntervals.push(now-lastMap);lastMap=now;}};
    const stop=()=>{if(stopped)return;stopped=true;cancelAnimationFrame(frame);if(timer)clearTimeout(timer);if(keys)clearInterval(keys);map.off('render',rendered);map.off('moveend',ended);window.removeEventListener('blur',blurred);if(moving)map.stop();};
    const abort=()=>{stop();if(!finished){finished=true;if(moving)map.jumpTo(pose);}};
    setCancel({run:abort});
    try {
      const before=await workload(map,selection);if(stopped)return;
      const beforeReady=ready(map,selection), visible=!document.hidden, focused=document.hasFocus();
      const layersBefore=layerIdentity(map), canvas=map.getCanvas();
      const visibleDataFeatures=map.queryRenderedFeatures().filter(feature=>feature.source.startsWith('external-')||feature.source.startsWith('kfm-')).length;
      start=performance.now();map.on('render',rendered);map.on('moveend',ended);window.addEventListener('blur',blurred);
      const sample=(now:number)=>{if(stopped)return;if(document.hidden)focusInterrupted=true;if(lastBrowser)browserIntervals.push(now-lastBrowser);lastBrowser=now;frame=requestAnimationFrame(sample);};
      frame=requestAnimationFrame(sample);
      if(moving && !interrupted)map.easeTo({...pose,center:[center.lng+.6,center.lat],duration:12000,easing:value=>value});
      if(interrupted){
        canvas.focus();
        const press=()=>{const key=['ArrowRight','ArrowDown','ArrowLeft','ArrowUp'][steps++%4],dispatchStart=performance.now();canvas.dispatchEvent(new KeyboardEvent('keydown',{key,code:key,keyCode:({ArrowRight:39,ArrowDown:40,ArrowLeft:37,ArrowUp:38} as Record<string,number>)[key],bubbles:true}));inputDispatchMaxMs=Math.max(inputDispatchMaxMs,performance.now()-dispatchStart);};
        // Send exactly 48 commands, including the first at the start, so the
        // final 12-second timer cannot race a 48th interval callback.
        press();keys=setInterval(()=>{if(steps<48)press();},250);
      }
      timer=setTimeout(async()=>{
        const elapsedMs=performance.now()-start;stop();
        try {
          const sourceAfter=await displaySignature(map), afterReady=ready(map,selectionRef.current);
          if(finished)return;
          const result:Result={format:'kfm-frame-pacing-v2',workload:before,browser:frameStatistics(browserIntervals,elapsedMs),map:frameStatistics(mapIntervals,elapsedMs),
            dataUnchanged:before.sourceDigest===sourceAfter,workloadUnchanged:samePacingWorkload(selection,selectionRef.current) && samePacingWorkload(layersBefore,layerIdentity(map)) && canvas.clientWidth===(before.viewport as number[])[0] && canvas.clientHeight===(before.viewport as number[])[1] && canvas.width===(before.canvas as number[])[0] && canvas.height===(before.canvas as number[])[1],
            readiness:{before:beforeReady,after:afterReady},visibility:{visible,focused,interrupted:focusInterrupted},elapsedMs,moving,interrupted,steps,movementEnds,inputDispatchMaxMs,
            visibleLayers:(map.getStyle().layers??[]).filter(layer=>map.getLayoutProperty(layer.id,'visibility')!=='none').length,selectedLayers,visibleDataFeatures,
            renderer:before.renderer as string,viewport:before.viewport as number[],canvasPixels:before.canvas as number[],url:location.href,recordedAt:new Date().toISOString()};
          setResult(result);
        }catch{if(!finished)setError('The workload comparison could not finish.');}
        if(finished)return;finished=true;if(moving)map.jumpTo(pose);setRunning(false);setCancel(null);
      },12000);
    }catch{abort();setRunning(false);setError('The map must be ready before measuring.');setCancel(null);}
  };
  const exportResult=()=>{if(!result)return;const url=URL.createObjectURL(new Blob([JSON.stringify(result,null,2)],{type:'application/json'}));const link=document.createElement('a');link.href=url;link.download='kfm-frame-pacing.json';link.click();setTimeout(()=>URL.revokeObjectURL(url),0);};
  return <aside aria-label="Frame pacing diagnostic" style={{position:'absolute',top:62,left:12,zIndex:1000,maxWidth:500,padding:12,color:'#eaf2f5',background:'#102332ee',border:'1px solid #8aa8b5',borderRadius:10,fontSize:13}}>
    <strong>Frame pacing · 12-second sample</strong><p>Keep this tab focused. Navigation acceptance requires matching workload records; idle water redraws intentionally run near 30 FPS.</p>
    <button disabled={!map||running} onClick={()=>void measure(false)}>Measure settled view</button>{' '}<button disabled={!map||running} onClick={()=>void measure(true)}>Measure continuous pan</button>{' '}<button disabled={!map||running} onClick={()=>void measure(true,true)}>Measure interrupted pan</button>{' '}<button disabled={!result||running} onClick={exportResult}>Download pacing record</button>
    <output aria-live="polite" data-frame-result={result?JSON.stringify(result):undefined} style={{display:'block',whiteSpace:'pre-wrap',marginTop:8}}>{running?'Measuring…':error??(result?`${result.moving?'Navigation':'Idle redraws'}: ${result.map.fps.toFixed(1)} FPS · p95 ${result.map.p95Ms.toFixed(1)} ms\nBrowser: ${result.browser.fps.toFixed(1)} FPS\n${result.selectedLayers} selected layers · ${result.visibleDataFeatures} visible data features\nData check: ${result.dataUnchanged?'unchanged':'changed during sample'} · foreground ${result.visibility.interrupted?'interrupted':'retained'}`:'Ready to measure')}</output>
  </aside>;
}
