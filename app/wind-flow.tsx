"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import type { Map as MapLibreMap } from "maplibre-gl";
import { readBoundedJson } from "./bounded-json";
import { interpolateWind, isWindField, WIND_API_PATH, WIND_REFERENCE_URL, WIND_SOURCE_URL, windVector, type WindField, type WindFrame } from "./wind-field";

type Particle = { longitude: number; latitude: number; age: number };
const LIMITS = { west: -101.8, east: -95, south: 37.3, north: 39.8 };
const makeParticle = (): Particle => ({
  longitude: LIMITS.west + Math.random() * (LIMITS.east - LIMITS.west),
  latitude: LIMITS.south + Math.random() * (LIMITS.north - LIMITS.south),
  age: Math.random() * 80,
});

function WindCanvas({ map, frame, playing }: { map: MapLibreMap | null; frame: WindFrame; playing: boolean }) {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const particlesRef = useRef<Particle[]>([]);
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas || !map) return;
    const context = canvas.getContext("2d");
    if (!context) return;
    let request = 0;
    let width = 0;
    let height = 0;
    const resize = () => {
      const host = map.getContainer();
      const scale = Math.min(window.devicePixelRatio || 1, 1.5);
      width = host.clientWidth; height = host.clientHeight;
      canvas.width = Math.round(width * scale); canvas.height = Math.round(height * scale);
      context.setTransform(scale, 0, 0, scale, 0, 0);
      if (!playing) drawStatic();
    };
    const drawStatic = () => {
      context.clearRect(0, 0, width, height);
      if (playing) return;
      for (const sample of frame.samples) {
        const [east, north] = windVector(sample);
        const point = map.project([sample.longitude, sample.latitude]);
        if (point.x < 0 || point.x > width || point.y < 0 || point.y > height) continue;
        const distance = Math.min(31, Math.max(9, sample.speedKmh * 0.6));
        const radians = Math.atan2(-north, east);
        context.save(); context.translate(point.x, point.y); context.rotate(radians);
        context.strokeStyle = "#8ce2e7"; context.lineWidth = 2; context.shadowColor = "#061c24"; context.shadowBlur = 6;
        context.beginPath(); context.moveTo(-distance / 2, 0); context.lineTo(distance / 2, 0);
        context.lineTo(distance / 2 - 6, -4); context.moveTo(distance / 2, 0); context.lineTo(distance / 2 - 6, 4); context.stroke();
        context.restore();
      }
    };
    const animate = () => {
      context.globalCompositeOperation = "destination-out";
      context.fillStyle = "rgba(0, 0, 0, .16)"; context.fillRect(0, 0, width, height);
      context.globalCompositeOperation = "source-over";
      if (particlesRef.current.length !== 130) particlesRef.current = Array.from({ length: 130 }, makeParticle);
      context.lineWidth = 1.5;
      for (let index = 0; index < particlesRef.current.length; index++) {
        let particle = particlesRef.current[index];
        const vector = interpolateWind(frame.samples, particle.longitude, particle.latitude);
        if (!vector || particle.age > 130) { particle = makeParticle(); particlesRef.current[index] = particle; }
        const current = map.project([particle.longitude, particle.latitude]);
        const [east, north] = interpolateWind(frame.samples, particle.longitude, particle.latitude) ?? [0, 0];
        const nextLongitude = particle.longitude + east * 0.00048;
        const nextLatitude = particle.latitude + north * 0.00038;
        if (nextLongitude < LIMITS.west || nextLongitude > LIMITS.east || nextLatitude < LIMITS.south || nextLatitude > LIMITS.north) {
          particlesRef.current[index] = makeParticle(); continue;
        }
        const next = map.project([nextLongitude, nextLatitude]);
        const speed = Math.hypot(east, north);
        context.strokeStyle = speed >= 45 ? "rgba(255, 214, 143, .85)" : speed >= 25 ? "rgba(147, 233, 232, .78)" : "rgba(114, 190, 216, .68)";
        context.beginPath(); context.moveTo(current.x, current.y); context.lineTo(next.x, next.y); context.stroke();
        particle.longitude = nextLongitude; particle.latitude = nextLatitude; particle.age += 1;
      }
      request = window.requestAnimationFrame(animate);
    };
    const onMove = () => { context.clearRect(0, 0, width, height); if (!playing) drawStatic(); };
    resize();
    const observer = new ResizeObserver(resize); observer.observe(map.getContainer());
    map.on("move", onMove);
    if (playing) request = window.requestAnimationFrame(animate);
    return () => { window.cancelAnimationFrame(request); observer.disconnect(); map.off("move", onMove); context.clearRect(0, 0, width, height); };
  }, [map, frame, playing]);
  return <canvas ref={canvasRef} className="wind-flow-canvas" aria-hidden="true" />;
}

export function WindFlow({ map, reducedMotion, onClose }: { map: MapLibreMap | null; reducedMotion: boolean; onClose: () => void }) {
  const [field, setField] = useState<WindField | null>(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [frameIndex, setFrameIndex] = useState(0);
  const [playing, setPlaying] = useState(false);
  const requestRef = useRef<AbortController | null>(null);
  const load = useCallback(async () => {
    requestRef.current?.abort();
    const controller = new AbortController(); requestRef.current = controller;
    setLoading(true); setError(""); setPlaying(false);
    try {
      const response = await fetch(WIND_API_PATH, { signal: controller.signal, cache: "no-store" });
      if (!response.ok) throw new Error("Wind forecast is unavailable.");
      const value = await readBoundedJson(response, 96 * 1024);
      if (!isWindField(value)) throw new Error("Wind forecast response was incomplete.");
      setField(value); setFrameIndex(0);
    } catch (cause) {
      if (!controller.signal.aborted) { setField(null); setError(cause instanceof Error ? cause.message : "Wind forecast is unavailable."); }
    } finally { if (!controller.signal.aborted) setLoading(false); }
  }, []);
  useEffect(() => { void load(); return () => requestRef.current?.abort(); }, [load]);
  useEffect(() => { if (reducedMotion) setPlaying(false); }, [reducedMotion]);
  useEffect(() => {
    if (!playing || !field || reducedMotion) return;
    const timer = window.setInterval(() => setFrameIndex((current) => (current + 1) % field.frames.length), 1350);
    return () => window.clearInterval(timer);
  }, [playing, field, reducedMotion]);
  const frame = field?.frames[Math.min(frameIndex, field.frames.length - 1)];
  return <>
    {frame && <WindCanvas map={map} frame={frame} playing={playing && !reducedMotion} />}
    <aside className="wind-flow-dock" aria-label="Kansas modeled wind display">
      <header><span>WIND FIELD · EXTERNAL MODEL</span><button type="button" onClick={onClose} aria-label="Close wind field">×</button></header>
      <h2>Follow the Kansas wind</h2>
      <p>{loading ? "Loading model samples…" : frame ? `${new Date(frame.validAt).toLocaleString()} · 10 m above ground · forecast` : "No wind field displayed"}</p>
      {frame && <div className="wind-flow-controls">
        <button type="button" onClick={() => setPlaying((value) => !value)} disabled={reducedMotion} aria-pressed={playing}>{playing ? "Ⅱ Pause" : "▶ Animate"}</button>
        <button type="button" onClick={() => { setPlaying(false); setFrameIndex((current) => Math.max(0, current - 1)); }} disabled={frameIndex === 0} aria-label="Previous forecast hour">‹</button>
        <input type="range" min="0" max={field!.frames.length - 1} value={frameIndex} onChange={(event) => { setPlaying(false); setFrameIndex(Number(event.target.value)); }} aria-label="Wind forecast hour" aria-valuetext={frame.validAt} />
        <button type="button" onClick={() => { setPlaying(false); setFrameIndex((current) => Math.min(field!.frames.length - 1, current + 1)); }} disabled={frameIndex === field!.frames.length - 1} aria-label="Next forecast hour">›</button>
        <span>{frameIndex + 1}/{field!.frames.length}</span>
      </div>}
      {frame && <div className="wind-flow-scale" aria-label="Wind speed color guide"><i /> <span>Slower</span><b>10 m wind speed · km/h</b><span>Faster</span></div>}
      {error && <p role="alert">{error} No wind animation is shown.</p>}
      <footer><span>{field ? `Retrieved ${new Date(field.retrievedAt).toLocaleString()}. ` : ""}{reducedMotion ? "Reduced motion: still arrows only. " : ""}Nine model samples; intervening paths are visual interpolation. Not observations, warnings, or KFM evidence.</span><a href={WIND_SOURCE_URL} target="_blank" rel="noreferrer">Forecast source ↗</a><a href={WIND_REFERENCE_URL} target="_blank" rel="noreferrer">Explore Earth ↗</a><button type="button" onClick={() => void load()} disabled={loading}>Refresh</button></footer>
    </aside>
  </>;
}
