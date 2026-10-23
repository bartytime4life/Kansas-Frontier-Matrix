"use client";
import { useEffect, useRef, useState } from "react";
/** Shares the actual metre-based map models; this view has no geographical
 * coordinates, historical dates, source status or recorded construction rate. */
export function TransportCrewPreview({ reducedMotion }: { reducedMotion: boolean }) {
  const host = useRef<HTMLDivElement>(null);
  const [mode, setMode] = useState<"road" | "rail">("road");
  const [error, setError] = useState(false);
  const [motion, setMotion] = useState(true);
  useEffect(() => {
    const element = host.current;
    if (!element) return;
    let disposed = false, frame = 0, cleanup = () => {};
    setError(false);
    void Promise.all([import("three"), import("./transport-crew-models")]).then(([THREE, { createTransportCrew }]) => {
      if (disposed) return;
      let renderer: InstanceType<typeof THREE.WebGLRenderer>;
      try { renderer = new THREE.WebGLRenderer({ alpha: false, antialias: true }); } catch { setError(true); return; }
      const scene = new THREE.Scene(); scene.background = new THREE.Color(0x222d2a);
      const camera = new THREE.PerspectiveCamera(37, 1, .1, 300);
      camera.up.set(0, 0, 1); camera.position.set(23, -37, 30); camera.lookAt(-9, 0, .7);
      renderer.setPixelRatio(Math.min(devicePixelRatio, 2)); renderer.toneMapping = THREE.ACESFilmicToneMapping;
      renderer.domElement.setAttribute("aria-hidden", "true"); element.append(renderer.domElement);
      const crew = createTransportCrew(mode, 2024, true); scene.add(crew.group);
      const light = new THREE.HemisphereLight(0xfff7e7, 0x66715e, 2.4); light.position.set(0, 0, 50); scene.add(light);
      const sun = new THREE.DirectionalLight(0xffeccb, 3); sun.position.set(-20, -40, 60); scene.add(sun);
      let last = 0;
      const draw = (time: number) => { if (disposed || document.hidden) return; crew.update(reducedMotion || !motion ? 0 : time / 1000); renderer.render(scene, camera); last = time; };
      const tick = (time: number) => { frame = 0; if (disposed || document.hidden) return; if (time - last > 32) draw(time); frame = requestAnimationFrame(tick); };
      const resize = () => { const width = Math.max(1, element.clientWidth); renderer.setSize(width, 260); camera.aspect = width / 260; camera.updateProjectionMatrix(); draw(performance.now()); };
      const visibility = () => { cancelAnimationFrame(frame); frame = 0; if (!document.hidden) { draw(performance.now()); if (!reducedMotion && motion) frame = requestAnimationFrame(tick); } };
      const observer = new ResizeObserver(resize); observer.observe(element); resize(); visibility();
      document.addEventListener("visibilitychange", visibility);
      cleanup = () => { observer.disconnect(); document.removeEventListener("visibilitychange", visibility); cancelAnimationFrame(frame); crew.dispose(); renderer.dispose(); renderer.domElement.remove(); };
    }).catch(() => { if (!disposed) setError(true); });
    return () => { disposed = true; cleanup(); };
  }, [mode, reducedMotion, motion]);
  return <div className="transport-crew-preview">
    <div className="transport-preview-controls"><strong>Equipment study · illustrative</strong><div>
      <button type="button" aria-pressed={mode === "road"} onClick={() => setMode("road")}>Road crew</button>
      <button type="button" aria-pressed={mode === "rail"} onClick={() => setMode("rail")}>Rail crew</button>
      <button type="button" aria-pressed={motion && !reducedMotion} disabled={reducedMotion} onClick={() => setMotion(v => !v)}>{motion && !reducedMotion ? "Pause motion" : "Enable motion"}</button>
    </div></div>
    <div ref={host} hidden={error} className="transport-preview-stage" role="img" aria-label={`Metre-based illustrative ${mode} equipment and crew model. No real site or historical build rate.`} />
    {error && <p role="status">3D preview is unavailable in this browser. Dates and study controls remain available.</p>}
    <p>Original 3D models in metres. Representative machinery and workers; this is a visual study, independent of the historical record.</p>
  </div>;
}
