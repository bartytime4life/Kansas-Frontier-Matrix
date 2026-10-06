"use client";
import { useEffect, useRef, useState } from "react";
import { intervalColor, meters, type Borehole } from "./subsurface-model";

/** A rotatable log diagram, not a georeferenced trajectory or an interpolated geological block. */
export default function SubsurfaceThree({ record, descriptionFilter, depthRange, exaggeration, depth }: { record: Borehole; descriptionFilter: string; depthRange: [number, number]; exaggeration: number; depth: number }) {
  const container = useRef<HTMLDivElement>(null);
  const [failure, setFailure] = useState("");
  const [retry, setRetry] = useState(0);
  const clipping = useRef<{ setDepth: (depth: number) => void } | null>(null);
  useEffect(() => {
    if (!container.current) return;
    let frame = 0;
    let disposed = false, cleanup: (() => void) | undefined;
    void Promise.all([import("three"), import("three/addons/controls/OrbitControls.js")]).then(([T, { OrbitControls }]) => {
      if (disposed || !container.current) return;
      let renderer: InstanceType<typeof T.WebGLRenderer>;
      try { renderer = new T.WebGLRenderer({ antialias: true, alpha: true }); } catch { setFailure("3D is unavailable on this device. The recorded intervals remain available in 2D."); return; }
      renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.5)); renderer.localClippingEnabled = true;
      renderer.domElement.tabIndex = 0; renderer.domElement.setAttribute("aria-label", "Rotatable recorded-depth diagram. Drag to rotate; scroll to zoom. Use the 2D intervals for keyboard inspection.");
      container.current.append(renderer.domElement);
      const scene = new T.Scene(), camera = new T.PerspectiveCamera(35, 1, .01, 200);
      const span = depthRange[1] - depthRange[0], scale = 3 / span, width = Math.min(.8, 5 * scale);
      const vertical = Math.min(exaggeration, 20);
      const clip = new T.Plane(new T.Vector3(0, -1, 0), -(depth - depthRange[0]) * scale * vertical);
      const group = new T.Group(); scene.add(group);
      const materials: InstanceType<typeof T.MeshStandardMaterial>[] = [], geometries: InstanceType<typeof T.BoxGeometry>[] = [];
      for (const i of record.intervals.filter(i => !descriptionFilter || i.description === descriptionFilter).slice(0, 500)) {
        const a = Math.max(depthRange[0], meters(i.top, record.depthUnit)), b = Math.min(depthRange[1], meters(i.bottom, record.depthUnit));
        if (b <= a) continue;
        const geometry = new T.BoxGeometry(width, (b - a) * scale * vertical, width);
        const material = new T.MeshStandardMaterial({ color: intervalColor(i), roughness: .95, metalness: 0, clippingPlanes: [clip], side: T.DoubleSide });
        const mesh = new T.Mesh(geometry, material); mesh.position.y = -(a + b - 2 * depthRange[0]) / 2 * scale * vertical;
        group.add(mesh); materials.push(material); geometries.push(geometry);
      }
      const ambient = new T.HemisphereLight(0xfff3d9, 0x536b65, 2.6); scene.add(ambient);
      const light = new T.DirectionalLight(0xffffff, 2); light.position.set(4, 3, 5); scene.add(light);
      camera.position.set(3 * vertical, -span * scale * vertical / 2 + vertical, 6 * vertical);
      const controls = new OrbitControls(camera, renderer.domElement); controls.target.set(0, -span * scale * vertical / 2, 0); controls.enableDamping = false;
      controls.minDistance = .2; controls.maxDistance = 100; controls.update();
      const render = () => { if (!disposed) renderer.render(scene, camera); };
      clipping.current = { setDepth: value => {
        cancelAnimationFrame(frame); const target = -(value - depthRange[0]) * scale * vertical;
        if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) { clip.constant = target; render(); return; }
        const start = performance.now(), from = clip.constant;
        const tick = (now: number) => { if (disposed) return; const t = Math.min(1, (now - start) / 180); clip.constant = from + (target - from) * (1 - (1 - t) ** 3); render(); if (t < 1) frame = requestAnimationFrame(tick); };
        frame = requestAnimationFrame(tick);
      } };
      const resize = () => { if (!container.current) return; const w = container.current.clientWidth, h = 310; renderer.setSize(w, h); camera.aspect = Math.max(1, w) / h; camera.updateProjectionMatrix(); render(); };
      const lost = (event: Event) => { event.preventDefault(); setFailure("3D graphics were interrupted. Continue in 2D or retry 3D."); };
      renderer.domElement.addEventListener("webglcontextlost", lost); controls.addEventListener("change", render);
      const observer = new ResizeObserver(resize); observer.observe(container.current); resize();
      cleanup = () => { observer.disconnect(); controls.dispose(); geometries.forEach(g => g.dispose()); materials.forEach(m => m.dispose()); renderer.dispose(); renderer.domElement.remove(); };
    }).catch(() => setFailure("The optional 3D viewer could not load. The 2D view remains available."));
    return () => { disposed = true; cancelAnimationFrame(frame); clipping.current = null; cleanup?.(); };
  // Depth scrubbing changes the clipping plane without rebuilding meshes or resetting the orbit.
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [record, descriptionFilter, depthRange, exaggeration, retry]);
  useEffect(() => { clipping.current?.setDepth(depth); }, [depth]);
  return <div><p><strong>Recorded-depth diagram · {record.id}</strong><br />Width is illustrative (5 m display width). No verified trajectory or elevation alignment. Colors encode descriptions; they are not core photographs. Vertical scale {Math.min(exaggeration, 20)}×.</p>
    {failure ? <p role="status">{failure} <button type="button" onClick={() => { setFailure(""); setRetry(v => v + 1); }}>Retry 3D</button></p> : null}<div ref={container} hidden={Boolean(failure)} />
  </div>;
}
