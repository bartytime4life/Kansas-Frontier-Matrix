"use client";
import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { meters, sourceLink, type Borehole, type DepthInterval } from "./subsurface-model";
import { MATERIALS, materialFor, materialInfo, materialPixels, type MaterialId } from "./subsurface-materials";
import { sliceIntervals, sliceHitVisible } from "./subsurface-slice";
import s from "./subsurface.module.css";

type ViewSettings = { opacity: number; exploded: boolean; slice: boolean; material: MaterialId | "all"; selected: number | null; depth: number };
type CameraAction = "oblique" | "front" | "top" | "left" | "right" | "in" | "out";
type SceneApi = { update: (settings: ViewSettings) => void; camera: (action: CameraAction) => void };

/** A textured extrusion of ONE log. Width, texture and spacing are illustrative, not resource geometry. */
export default function SubsurfaceThree({ record, descriptionFilter, depthRange, exaggeration, depth, slice, selectedIndex, onDepth, onSlice, onInspect }: { record: Borehole; descriptionFilter: string; depthRange: [number, number]; exaggeration: number; depth: number; slice: boolean; selectedIndex: number | null; onDepth: (depth: number) => void; onSlice: (enabled: boolean) => void; onInspect: (interval: DepthInterval) => void }) {
  const container = useRef<HTMLDivElement>(null), api = useRef<SceneApi | null>(null);
  const [failure, setFailure] = useState(""), [retry, setRetry] = useState(0);
  const [opacity, setOpacity] = useState(.95), [exploded, setExploded] = useState(false);
  const [materialChoice, setMaterialChoice] = useState<{recordId:string; value:MaterialId | "all"}>({recordId:record.id,value:"all"});
  const material = materialChoice.recordId === record.id ? materialChoice.value : "all";
  const setMaterial = (value: MaterialId | "all") => setMaterialChoice({recordId:record.id,value});
  const settings = useRef<ViewSettings>({ opacity, exploded, slice, material, selected: selectedIndex, depth });
  useEffect(() => { settings.current = { opacity, exploded, slice, material, selected: selectedIndex, depth }; }, [opacity, exploded, slice, material, selectedIndex, depth]);
  const intervals = useMemo(() => sliceIntervals(record, depthRange)
    .filter(({ interval }) => !descriptionFilter || interval.description === descriptionFilter)
    .map(row => ({ ...row, material: materialFor(row.interval, record.kind) })), [record, descriptionFilter, depthRange]);
  const rendered = useMemo(() => intervals.slice(0, 500), [intervals]);
  const selected = selectedIndex === null ? null : record.intervals[selectedIndex];
  const pick = useCallback((index: number) => { const interval = record.intervals[index]; if (interval) onInspect(interval); }, [onInspect, record]);
  const pickRef = useRef(pick);
  useEffect(() => { pickRef.current = pick; }, [pick]);

  useEffect(() => {
    if (!container.current) return;
    let disposed = false, cleanup: (() => void) | undefined;
    void Promise.all([import("three"), import("three/addons/controls/OrbitControls.js")]).then(([T, { OrbitControls }]) => {
      if (disposed || !container.current) return;
      let renderer: InstanceType<typeof T.WebGLRenderer>;
      try { renderer = new T.WebGLRenderer({ antialias: true }); } catch { setFailure("3D is unavailable on this device. Use the interval list or Columns & section."); return; }
      const resources: { dispose: () => void }[] = [];
      // Register partial cleanup before allocating scene resources so initialization failure is safe.
      cleanup = () => { resources.forEach(r => r.dispose()); renderer.dispose(); renderer.domElement.remove(); };
      renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.5)); renderer.localClippingEnabled = true;
      renderer.domElement.tabIndex = 0; renderer.domElement.setAttribute("aria-label", "Underground recorded-depth material diagram. Drag to orbit, scroll to zoom. Camera buttons and the layer list offer keyboard alternatives.");
      container.current.append(renderer.domElement);
      const scene = new T.Scene(); scene.background = new T.Color("#09191e");
      const camera = new T.PerspectiveCamera(38, 1, .01, 500);
      const span = depthRange[1] - depthRange[0], scale = 3 / span, vertical = Math.min(exaggeration, 20), height = 3 * vertical;
      const group = new T.Group(); scene.add(group);
      const textureCache = new Map<MaterialId, InstanceType<typeof T.DataTexture>>();
      const meshes: { mesh: InstanceType<typeof T.Mesh>; paint: InstanceType<typeof T.MeshStandardMaterial>; clip: InstanceType<typeof T.Plane>; center: number; id: MaterialId; index: number; order: number }[] = [];
      for (const [order, row] of rendered.entries()) {
        const a = Math.max(depthRange[0], meters(row.interval.top, record.depthUnit)), b = Math.min(depthRange[1], meters(row.interval.bottom, record.depthUnit));
        const geometry = new T.BoxGeometry(2.8, (b - a) * scale * vertical, 1.8); resources.push(geometry);
        let texture = textureCache.get(row.material);
        if (!texture) {
          texture = new T.DataTexture(materialPixels(row.material), 64, 64); texture.colorSpace = T.SRGBColorSpace;
          texture.wrapS = texture.wrapT = T.RepeatWrapping; texture.magFilter = T.LinearFilter; texture.minFilter = T.LinearFilter; texture.needsUpdate = true;
          textureCache.set(row.material, texture); resources.push(texture);
        }
        const clip = new T.Plane(new T.Vector3(0, -1, 0), 0);
        const paint = new T.MeshStandardMaterial({ map: texture, bumpMap: texture, bumpScale: row.material === "unknown" || row.material === "inventory" ? 0 : .035, roughness: .95, metalness: 0, transparent: true, side: T.DoubleSide }); resources.push(paint);
        const mesh = new T.Mesh(geometry, paint); const center = -(a + b - 2 * depthRange[0]) / 2 * scale * vertical;
        mesh.position.y = center; mesh.userData.index = row.index; group.add(mesh);
        meshes.push({ mesh, paint, clip, center, id: row.material, index: row.index, order });
      }
      const grid = new T.GridHelper(8, 16, "#77bcb7", "#203e47"); scene.add(grid); resources.push(grid.geometry, ...(Array.isArray(grid.material) ? grid.material : [grid.material]));
      const outlineBox = new T.BoxGeometry(2.82, height, 1.82);
      const outlineGeometry = new T.EdgesGeometry(outlineBox); outlineBox.dispose();
      const outlineMaterial = new T.LineBasicMaterial({ color: "#64888a", transparent: true, opacity: .4 });
      const outline = new T.LineSegments(outlineGeometry, outlineMaterial); outline.position.y = -height / 2; scene.add(outline); resources.push(outlineGeometry, outlineMaterial);
      // This outline is a UI cut guide, never a geological boundary or a pick target.
      const cutGeometry = new T.BufferGeometry().setFromPoints([
        new T.Vector3(-1.46,0,-.96), new T.Vector3(1.46,0,-.96), new T.Vector3(1.46,0,.96), new T.Vector3(-1.46,0,.96),
      ]);
      const cutPaint = new T.LineBasicMaterial({color:"#f4bd6c",depthTest:false,transparent:true,opacity:.95});
      const cutGuide = new T.LineLoop(cutGeometry,cutPaint); cutGuide.renderOrder=10; scene.add(cutGuide); resources.push(cutGeometry,cutPaint);
      scene.add(new T.HemisphereLight(0xffe9c9, 0x304854, 2.5));
      const light = new T.DirectionalLight(0xffffff, 3); light.position.set(4, 5, 6); scene.add(light);
      const rim = new T.DirectionalLight(0x73b3c2, 1.4); rim.position.set(-4, -2, -3); scene.add(rim);
      const controls = new OrbitControls(camera, renderer.domElement); resources.push(controls);
      controls.enableDamping = false; controls.minDistance = .3; controls.maxDistance = 180;
      const render = () => { if (!disposed && !document.hidden) renderer.render(scene, camera); };
      let currentExplosion = false;
      const separation = Math.min(.16, 3 / Math.max(1, rendered.length - 1));
      const totalHeight = () => height + (currentExplosion ? Math.max(0, rendered.length - 1) * separation : 0);
      const moveCamera = (action: CameraAction) => {
        const target = controls.target, extent = Math.max(4, totalHeight());
        if (action === "in" || action === "out") camera.position.sub(target).multiplyScalar(action === "in" ? .8 : 1.25).add(target);
        else if (action === "left" || action === "right") { const delta = camera.position.clone().sub(target); delta.applyAxisAngle(new T.Vector3(0,1,0), action === "left" ? -.3 : .3); camera.position.copy(target).add(delta); }
        else { target.set(0, -totalHeight()/2, 0); camera.position.set(action === "front" || action === "top" ? 0 : extent, action === "top" ? extent * 1.8 : target.y + (action === "front" ? 0 : extent * .45), action === "top" ? .01 : extent * 1.8); }
        controls.update(); render();
      };
      const update = (v: ViewSettings) => {
        currentExplosion = v.exploded && !v.slice;
        outline.visible = !currentExplosion;
        cutGuide.visible = v.slice && meshes.length > 0; cutGuide.position.y = -(v.depth-depthRange[0])*scale*vertical;
        for (const row of meshes) {
          row.mesh.position.y = row.center - (currentExplosion ? row.order * separation : 0);
          row.mesh.visible = v.material === "all" || v.material === row.id;
          row.paint.opacity = v.opacity; row.paint.depthWrite = v.opacity >= .99;
          row.clip.constant = -(v.depth - depthRange[0]) * scale * vertical;
          const wasSliced = Boolean(row.paint.clippingPlanes?.length);
          row.paint.clippingPlanes = v.slice ? [row.clip] : [];
          if (wasSliced !== v.slice) row.paint.needsUpdate = true;
          row.paint.emissive.set(row.index === v.selected ? "#55451b" : "#000000");
        }
        render();
      };
      api.current = { update, camera: moveCamera }; update(settings.current); moveCamera("oblique");
      const resize = () => { if (!container.current) return; const w = Math.max(1, container.current.clientWidth), h = w < 600 ? 330 : 440; renderer.setSize(w, h); camera.aspect = w/h; camera.updateProjectionMatrix(); render(); };
      const lost = (event: Event) => { event.preventDefault(); setFailure("3D graphics were interrupted. Use the recorded intervals below, or retry."); };
      const ray = new T.Raycaster(), pointer = new T.Vector2(); let down = [0,0];
      const onDown = (event: PointerEvent) => { down = [event.clientX,event.clientY]; };
      const onUp = (event: PointerEvent) => {
        if (Math.hypot(event.clientX-down[0],event.clientY-down[1]) > 5) return;
        const bounds = renderer.domElement.getBoundingClientRect(); pointer.set((event.clientX-bounds.left)/bounds.width*2-1, -(event.clientY-bounds.top)/bounds.height*2+1); ray.setFromCamera(pointer,camera);
        const hit = ray.intersectObjects(meshes.filter(row => row.mesh.visible && row.paint.opacity > 0).map(row => row.mesh)).find(h => sliceHitVisible(h.point.y,settings.current.slice,settings.current.depth,depthRange[0],scale,vertical));
        if (hit) pickRef.current(hit.object.userData.index as number);
      };
      const onKey = (event: KeyboardEvent) => { const actions: Record<string,CameraAction> = { ArrowLeft:"left",ArrowRight:"right","+":"in","=":"in","-":"out",Home:"oblique" }; if(actions[event.key]) { event.preventDefault(); moveCamera(actions[event.key]); } };
      renderer.domElement.addEventListener("pointerdown",onDown); renderer.domElement.addEventListener("pointerup",onUp); renderer.domElement.addEventListener("keydown",onKey); renderer.domElement.addEventListener("webglcontextlost", lost);
      controls.addEventListener("change", render); document.addEventListener("visibilitychange",render);
      const observer = new ResizeObserver(resize); observer.observe(container.current); resize();
      const disposeResources = cleanup;
      cleanup = () => { observer.disconnect(); document.removeEventListener("visibilitychange",render); renderer.domElement.removeEventListener("pointerdown",onDown); renderer.domElement.removeEventListener("pointerup",onUp); renderer.domElement.removeEventListener("keydown",onKey); renderer.domElement.removeEventListener("webglcontextlost",lost); controls.removeEventListener("change", render); disposeResources(); };
    }).catch(() => { cleanup?.(); cleanup = undefined; if (!disposed) setFailure("The optional 3D viewer could not load. The recorded interval list remains available."); });
    return () => { disposed = true; api.current = null; cleanup?.(); };
  }, [record, rendered, depthRange, exaggeration, retry]);
  // Scrubbing, material isolation and opacity reuse the renderer and keep the camera position.
  useEffect(() => { api.current?.update(settings.current); }, [depth, opacity, exploded, slice, material, selectedIndex]);

  return <section className={s.materialExplorer} aria-label="3D slice and material inspection">
    <header className={s.materialHeading}><div><span>3D SLICE · {record.kind === "core" ? "INVENTORY ENVELOPE" : "RECORDED LOG"}</span><h3>{record.name}</h3></div><a href={sourceLink(record.sourceUrl) ?? undefined} target="_blank" rel="noreferrer">Source log ↗</a></header>
    <p className={s.modelBoundary}>{record.kind === "core" ? "One core inventory envelope, not verified recovered rock." : "One recorded log; horizontal width and material textures are illustrative."} Empty intervals remain unknown. This is separate from the geographic section across records.</p>
    <div className={s.sliceDepthStrip} data-sliced={slice}>
      <label htmlFor="recorded-slice-depth">Slice depth <output>{depth.toFixed(2)} <small>m</small></output></label>
      <input id="recorded-slice-depth" aria-label="Slice depth in metres" aria-valuetext={`${depth.toFixed(2)} metres${slice ? ", material above hidden" : ", whole column shown"}`} type="range" min={depthRange[0]} max={depthRange[1]} step={(depthRange[1]-depthRange[0])/1000} value={depth} disabled={!rendered.length} onChange={e => onDepth(Number(e.target.value))} />
      <button type="button" disabled={!slice && !rendered.length} aria-pressed={slice} onClick={() => onSlice(!slice)}>{slice ? "Show whole column" : "Start 3D slice"}</button>
      <p>{slice ? "Slicing on · drag the slider to hide recorded material above that depth. Amber outline marks the cut." : "Whole column shown · start a slice to hide material above the chosen recorded depth."}</p>
    </div>
    <div className={s.modelCamera} aria-label="Underground camera controls">{([['oblique','Reset view'],['left','Rotate left'],['right','Rotate right'],['in','Zoom in'],['out','Zoom out']] as const).map(([action,label]) => <button type="button" key={action} onClick={() => api.current?.camera(action)} disabled={!!failure}>{label}</button>)}</div>
    <div className={s.modelStage}><div ref={container} hidden={Boolean(failure)} /><div className={s.modelStamp}>DEPTH {depthRange.join("–")} m · {Math.min(exaggeration,20)}× vertical display{exploded && !slice ? " · separated spacing" : ""}<br />{record.depthReference} · horizontal extent unknown{slice ? ` · CUT ${depth.toFixed(2)} m` : " · WHOLE COLUMN"}</div></div>
    {failure && <p role="status">{failure} <button type="button" onClick={() => { setFailure(""); setRetry(v => v+1); }}>Retry 3D</button></p>}
    {slice && rendered.length > 0 && !rendered.some(row => row.bottom > depth) && <p role="status">All displayed intervals are above this cut. Drag Slice depth upward or show the whole column.</p>}
    {!rendered.length && <p role="status">No logged interval intersects this depth and description filter. Use Fit recorded depths, adjust the filter, or choose another record.</p>}
    {selected && <article className={s.selectedLayer} aria-live="polite"><strong>{selected.top}–{selected.bottom} {record.depthUnit} · {materialInfo(materialFor(selected,record.kind)).label}</strong><p>Original log: {selected.description}</p>{selected.interpreted && <p>KGS interpretation: {selected.interpreted}</p>}<small>{slice && meters(selected.bottom, record.depthUnit) <= depth ? "Selected interval is above the cut and hidden in the model. " : ""}Record date: {record.sourceTime || "not supplied"}. This interval describes the record location, not a surrounding deposit.</small></article>}
    <details className={s.sliceAdvanced}><summary>Appearance &amp; materials{material !== "all" ? ` · ${materialInfo(material).label} only` : ""}</summary>
      <div className={s.modelControls}>
        <button type="button" aria-pressed={exploded} disabled={slice} onClick={() => setExploded(v => !v)}>Separate layers</button>
        <label>Opacity <input type="range" min="0" max="100" value={Math.round(opacity*100)} onChange={e => setOpacity(Number(e.target.value)/100)} />{Math.round(opacity*100)}%</label>
        <label>Material <select value={material} onChange={e => setMaterial(e.target.value as MaterialId | "all")}><option value="all">All materials</option>{MATERIALS.map(m => <option key={m.id} value={m.id} disabled={!rendered.some(row => row.material === m.id)}>{m.label} · {rendered.filter(row => row.material === m.id).length} intervals</option>)}</select></label>
      </div>
      <div className={s.modelCamera} aria-label="Additional camera views">{([['front','Front'],['top','Top']] as const).map(([action,label]) => <button type="button" key={action} onClick={() => api.current?.camera(action)} disabled={!!failure}>{label}</button>)}</div>
      <div className={s.materialLegend}>{MATERIALS.filter(m => rendered.some(row => row.material === m.id)).map(m => <button type="button" key={m.id} aria-pressed={material === m.id} onClick={() => setMaterial(material === m.id ? "all" : m.id)}><i style={{ background:m.color }} />{m.label}</button>)}</div>
      <p className={s.muted}>{rendered.length}/{intervals.length} intervals in this depth/description window drawn (500 maximum). {record.kind === "core" ? "Violet volumes represent inventory envelopes, not the recovered rock type." : "Textures encode unambiguous words in the original log. Mixed, qualified and fluid descriptions remain neutral."} Selection glows amber. Rotation and zoom render on demand.</p>
    </details>
    <details className={s.layerList} open={Boolean(failure)}><summary>Recorded intervals · keyboard view</summary><div>{rendered.filter(row => material === "all" || row.material === material).map(row => <button type="button" key={row.index} aria-pressed={selectedIndex === row.index} onClick={() => pick(row.index)}><i style={{background:materialInfo(row.material).color}} /><span><strong>{row.interval.top}–{row.interval.bottom} {record.depthUnit}</strong><small>{row.interval.description}</small></span></button>)}</div></details>
    <details><summary>Source interpretation limits</summary><p>Oil, gas, groundwater, ore and mine geometry require their own measured or reviewed source geometry. A fluid word in a log is not a reservoir boundary; a core inventory is not an ore body. No inferred resource pockets, flooded layers or tunnels are drawn. Select a source interval to read its original description. SSURGO soil components and geophysical measurements remain in their separate tabs.</p><p>Continuous extrapolation is held until a qualified correlation model supplies elevation registration, uncertainty, coverage limits and source references. This view makes no claim about mineral ownership, reserves, drilling or excavation safety.</p></details>
  </section>;
}
