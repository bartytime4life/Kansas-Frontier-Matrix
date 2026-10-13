"use client";
import { useEffect, useState } from "react";
import type { Map as GLMap, GeoJSONSource } from "./maplibre-seam";
import { uploadedGeoJSON } from "./map-performance";

export function frameStatistics(intervals: readonly number[], elapsed: number) {
  const sorted = [...intervals].sort((a, b) => a - b);
  return { frames: intervals.length, fps: elapsed > 0 ? intervals.length * 1000 / elapsed : 0,
    p95Ms: sorted.length ? sorted[Math.min(sorted.length - 1, Math.floor(sorted.length * .95))] : 0,
    maxMs: sorted.at(-1) ?? 0, over25ms: intervals.filter(value => value > 25).length };
}
export async function displaySignature(map: GLMap) {
  const style = map.getStyle();
  const data = Object.keys(style.sources).sort().map(id => {
    const source = map.getSource(id);
    const collection = source?.type === "geojson" ? uploadedGeoJSON(source as GeoJSONSource) : undefined;
    return [id, collection ?? style.sources[id]];
  });
  const digest = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(JSON.stringify(data)));
  return [...new Uint8Array(digest)].map(byte => byte.toString(16).padStart(2, "0")).join("");
}
type Result = { browser: ReturnType<typeof frameStatistics>; map: ReturnType<typeof frameStatistics>; dataUnchanged: boolean; visibleLayers: number; selectedLayers:number; visibleDataFeatures:number; renderer: string; viewport: number[]; canvasPixels: number[]; moving: boolean; interrupted:boolean; steps:number; movementEnds:number; inputDispatchMaxMs:number };
/** Explicit diagnostic only; no listeners, polling or telemetry in ordinary views. */
export function FrameCheck({ map, selectedLayers }: { map: GLMap | null; selectedLayers:number }) {
  const [running, setRunning] = useState(false), [result, setResult] = useState<Result | null>(null), [error, setError] = useState<string | null>(null);
  const [cancel, setCancel] = useState<{run:()=>void} | null>(null);
  useEffect(() => () => cancel?.run(), [cancel]);
  const measure = async (moving: boolean, interrupted = false) => {
    if (!map || running) return;
    setRunning(true);setResult(null);setError(null);
    const center = map.getCenter(); const pose = {center:[center.lng,center.lat] as [number,number],zoom:map.getZoom(),bearing:map.getBearing(),pitch:map.getPitch()};
    let stopped=false, frame=0, timer:ReturnType<typeof setTimeout> | undefined, start=0, lastBrowser=0, lastMap=0, steps=0;
    let keys:ReturnType<typeof setInterval> | undefined, movementEnds=0, inputDispatchMaxMs=0;
    const ended=()=>{movementEnds++;};
    const browserIntervals:number[]=[],mapIntervals:number[]=[];
    const rendered=()=>{const now=performance.now();if(start && now>=start){if(lastMap)mapIntervals.push(now-lastMap);lastMap=now;}};
    const stop=()=>{if(stopped)return;stopped=true;cancelAnimationFrame(frame);if(timer)clearTimeout(timer);if(keys)clearInterval(keys);map.off("render",rendered);map.off("moveend",ended);if(moving)map.stop();};
    setCancel({run:stop});
    try {
      const before=await displaySignature(map);if(stopped)return;
      const canvas=map.getCanvas();const gl=canvas.getContext("webgl2");const debug=gl?.getExtension("WEBGL_debug_renderer_info");
      const renderer=debug ? String(gl!.getParameter(debug.UNMASKED_RENDERER_WEBGL)) : "Unavailable";
      const visibleDataFeatures=map.queryRenderedFeatures().filter(feature=>feature.source.startsWith("external-")||feature.source.startsWith("kfm-")).length;
      const visibleLayers=(map.getStyle().layers??[]).filter(layer=>map.getLayoutProperty(layer.id,"visibility")!=="none").length;
      start=performance.now();map.on("render",rendered);map.on("moveend",ended);
      const sample=(now:number)=>{if(stopped)return;if(document.hidden){stop();setError("Keep the measured tab visible for the full sample.");setRunning(false);return;}if(lastBrowser)browserIntervals.push(now-lastBrowser);lastBrowser=now;frame=requestAnimationFrame(sample);};
      frame=requestAnimationFrame(sample);
      if(moving && !interrupted)map.easeTo({...pose,center:[center.lng+.6,center.lat],duration:12000,easing:value=>value});
      if(interrupted){
        canvas.focus();
        keys=setInterval(()=>{const key=["ArrowRight","ArrowDown","ArrowLeft","ArrowUp"][steps++%4], dispatchStart=performance.now();canvas.dispatchEvent(new KeyboardEvent("keydown",{key,code:key,keyCode:({ArrowRight:39,ArrowDown:40,ArrowLeft:37,ArrowUp:38} as Record<string,number>)[key],bubbles:true}));inputDispatchMaxMs=Math.max(inputDispatchMaxMs,performance.now()-dispatchStart);},250);
      }
      timer=setTimeout(async()=>{
        const elapsed=performance.now()-start;stop();
        try {
          const after=await displaySignature(map);
          setResult({browser:frameStatistics(browserIntervals,elapsed),map:frameStatistics(mapIntervals,elapsed),dataUnchanged:before===after,visibleLayers,selectedLayers,visibleDataFeatures,renderer,viewport:[canvas.clientWidth,canvas.clientHeight],canvasPixels:[canvas.width,canvas.height],moving,interrupted,steps,movementEnds,inputDispatchMaxMs});
        }catch{setError("The data comparison could not finish.");}
        if(moving)map.jumpTo(pose);setRunning(false);setCancel(null);
      },12000);
    }catch{stop();setRunning(false);setError("The map must be ready before measuring.");setCancel(null);}
  };
  return <aside aria-label="Frame pacing diagnostic" style={{position:"absolute",top:62,left:12,zIndex:1000,maxWidth:500,padding:12,color:"#eaf2f5",background:"#102332ee",border:"1px solid #8aa8b5",borderRadius:10,fontSize:13}}>
    <strong>Frame pacing · 12-second sample</strong><p>Keep this tab visible. Pan samples test navigation; an idle map can sleep.</p>
    <button disabled={!map||running} onClick={()=>void measure(false)}>Measure settled view</button>{" "}<button disabled={!map||running} onClick={()=>void measure(true)}>Measure continuous pan</button>{" "}<button disabled={!map||running} onClick={()=>void measure(true,true)}>Measure interrupted pan</button>
    <output aria-live="polite" data-frame-result={result?JSON.stringify(result):undefined} style={{display:"block",whiteSpace:"pre-wrap",marginTop:8}}>{running?"Measuring…":error??(result?`${result.moving ? "Navigation" : "Idle redraws"}: ${result.map.fps.toFixed(1)} FPS · p95 ${result.map.p95Ms.toFixed(1)} ms\nBrowser: ${result.browser.fps.toFixed(1)} FPS\n${result.selectedLayers} selected layers · ${result.visibleDataFeatures} visible data features\nData check: ${result.dataUnchanged ? "unchanged" : "changed during sample"}`:"Ready to measure")}</output>
  </aside>;
}
