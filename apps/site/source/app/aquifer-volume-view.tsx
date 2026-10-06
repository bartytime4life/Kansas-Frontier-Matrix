"use client";
import { useEffect, useRef, useState } from "react";
import type { Map as MapLibreMap } from "maplibre-gl";
import { projectVolumePosition, volumeDepthScale } from "./aquifer-volume";
import { materialFor, materialInfo } from "./subsurface-materials";
import { meters, type Borehole, type DepthInterval } from "./subsurface-model";
import { KGS_ATLAS_URL } from "./aquifer-layers";
import s from "./subsurface.module.css";
import { aquiferGeometries } from "./aquifer-volume-mesh";
import { startAquiferView, type AquiferViewSnapshot } from "./aquifer-view-session";
type Snapshot = AquiferViewSnapshot<HTMLCanvasElement>;
type CameraAction="reset"|"top"|"side"|"left"|"right"|"in"|"out";
type Settings={surface:number;water:number;scale:number;logs:boolean};
export default function AquiferVolumeView({map,records,onFlatMap,onLocate,onInspect}:{map:MapLibreMap|null;records:Borehole[];onFlatMap:()=>void;onLocate:(point:[number,number])=>void;onInspect:(record:Borehole,interval?:DepthInterval)=>void}){
  const [snapshot,setSnapshot]=useState<Snapshot|null>(null),[status,setStatus]=useState("Preparing the current locator area…"),[retry,setRetry]=useState(0);
  const [surfaceStatus,setSurfaceStatus]=useState("");
  const [surface,setSurface]=useState(.55),[water,setWater]=useState(.55),[scale,setScale]=useState(50),[logs,setLogs]=useState(true);
  const [failure,setFailure]=useState(""),[selection,setSelection]=useState<string|null>(null);
  const host=useRef<HTMLDivElement>(null),api=useRef<{camera:(action:CameraAction)=>void;update:(v:Settings)=>void;setSurface:(image:HTMLCanvasElement|null)=>void}|null>(null);
  const values=useRef<Settings>({surface,water,scale,logs});
  const inspectRef=useRef(onInspect);
  const snapshotRef=useRef(snapshot);
  const volume=snapshot?.volume;
  useEffect(()=>{values.current={surface,water,scale,logs};},[surface,water,scale,logs]);
  useEffect(()=>{inspectRef.current=onInspect;},[onInspect]);
  useEffect(()=>{snapshotRef.current=snapshot;},[snapshot]);
  useEffect(()=>{let cancelled=false;queueMicrotask(()=>{if(!cancelled)setSelection(null);});return()=>{cancelled=true;};},[volume]);
  useEffect(()=>{
    if(!map)return;
    let cancelled=false;
    let worker:Worker;
    try{worker=new Worker(new URL("./aquifer-volume-worker.ts",import.meta.url),{type:"module"});}catch{queueMicrotask(()=>{if(!cancelled)setStatus("Aquifer preparation worker unavailable. The locator and logs remain usable.");});return()=>{cancelled=true;};}
    const stop=startAquiferView<HTMLCanvasElement>({map,worker,onSnapshot:setSnapshot,onStatus:setStatus,onSurfaceStatus:setSurfaceStatus,sampleSurface:()=>{
      const source=map.getCanvas(),image=document.createElement("canvas");
      const ratio=Math.min(1,1024/Math.max(source.width,source.height));image.width=Math.max(1,Math.round(source.width*ratio));image.height=Math.max(1,Math.round(source.height*ratio));
      const ctx=image.getContext("2d");if(!ctx)throw new Error("Surface capture unavailable");
      ctx.drawImage(source,0,0,image.width,image.height);
      // Only read back a complete frame; failure does not hold aquifer geometry.
      ctx.getImageData(0,0,1,1);return image;
    }});
    return()=>{cancelled=true;stop();worker.terminate();};
  },[map,retry]);

  useEffect(()=>{
    if(!volume||!host.current)return;
    setFailure("");
    let disposed=false,cleanup:(()=>void)|undefined;
    void Promise.all([import("three"),import("three/addons/controls/OrbitControls.js")]).then(([T,{OrbitControls}])=>{
      if(disposed||!host.current)return;
      const renderer=new T.WebGLRenderer({antialias:true});renderer.setPixelRatio(Math.min(devicePixelRatio,1.5));
      const resources:{dispose:()=>void}[]=[];cleanup=()=>{resources.forEach(r=>r.dispose());renderer.dispose();renderer.domElement.remove();};
      renderer.domElement.tabIndex=0;renderer.domElement.setAttribute("aria-label","Aquifer uncertainty envelope beneath the captured 2D surface. Drag to orbit; use camera buttons or the region list for keyboard access.");host.current.append(renderer.domElement);
      const scene=new T.Scene();scene.background=new T.Color("#081b24");const camera=new T.PerspectiveCamera(40,1,.01,500);
      const controls=new OrbitControls(camera,renderer.domElement);controls.enableDamping=false;controls.minDistance=.2;controls.maxDistance=150;resources.push(controls);
      const bounds=volume.bounds,k=volumeDepthScale(bounds);
      const north=projectVolumePosition(bounds[0],bounds[3],bounds).z,south=projectVolumePosition(bounds[0],bounds[1],bounds).z;
      const planeGeometry=new T.PlaneGeometry(6,south-north);planeGeometry.rotateX(-Math.PI/2);resources.push(planeGeometry);
      const planePaint=new T.MeshBasicMaterial({color:"#83a4a7",transparent:true,opacity:values.current.surface*.15,side:T.DoubleSide,depthWrite:false});resources.push(planePaint);
      let surfaceTexture:InstanceType<typeof T.CanvasTexture>|null=null;
      resources.push({dispose:()=>surfaceTexture?.dispose()});
      const plane=new T.Mesh(planeGeometry,planePaint);plane.position.y=.0005;plane.renderOrder=3;scene.add(plane);
      const borderGeom=new T.EdgesGeometry(planeGeometry),borderPaint=new T.LineBasicMaterial({color:"#aedbd2"});resources.push(borderGeom,borderPaint);const border=new T.LineSegments(borderGeom,borderPaint);border.position.y=.001;scene.add(border);
      const volumeGroup=new T.Group(),logGroup=new T.Group();scene.add(volumeGroup,logGroup);
      const waters:InstanceType<typeof T.MeshStandardMaterial>[]=[],pickable:InstanceType<typeof T.Mesh>[]=[];
      for(const {envelope,geometry} of aquiferGeometries(T,volume)){
        resources.push(geometry);
        const paint=new T.MeshStandardMaterial({color:"#238da9",roughness:.65,metalness:0,transparent:true,opacity:values.current.water,depthWrite:false,side:T.DoubleSide});waters.push(paint);resources.push(paint);
        const mesh=new T.Mesh(geometry,paint);mesh.userData.envelope=envelope;mesh.renderOrder=1;volumeGroup.add(mesh);pickable.push(mesh);
      }
      let drawnIntervals=0;
      const logDepthLimit=volume.envelopes.length?Math.max(...volume.envelopes.map(e=>e.deepMeters))+50:500;
      for(const record of records.slice(0,50)){
        const [lon,lat]=record.coordinates;if(lon<bounds[0]||lon>bounds[2]||lat<bounds[1]||lat>bounds[3])continue;
        const p=projectVolumePosition(lon,lat,bounds);
        for(const interval of record.intervals){if(drawnIntervals>=400)break;drawnIntervals++;
          const top=meters(interval.top,record.depthUnit),bottom=Math.min(logDepthLimit,meters(interval.bottom,record.depthUnit));if(bottom<=top)continue;
          const geometry=new T.BoxGeometry(.027,(bottom-top)*k,.027),paint=new T.MeshBasicMaterial({color:materialInfo(materialFor(interval,record.kind)).color});resources.push(geometry,paint);
          const mesh=new T.Mesh(geometry,paint);mesh.position.set(p.x,-(top+bottom)/2*k,p.z);mesh.userData.record=record;mesh.userData.interval=interval;logGroup.add(mesh);pickable.push(mesh);
        }
      }
      scene.add(new T.HemisphereLight(0xd2eeff,0x194955,2.5));const light=new T.DirectionalLight(0xffffff,2);light.position.set(4,6,3);scene.add(light);
      const render=()=>{if(!disposed&&!document.hidden)renderer.render(scene,camera);};
      const deepest=Math.max(1,...volume.envelopes.map(e=>e.deepMeters));
      const orient=(action:CameraAction)=>{
        const center=controls.target,span=Math.max(6,south-north,deepest*k*values.current.scale),y=-deepest*k*values.current.scale/2;
        if(action==="left"||action==="right"){const d=camera.position.clone().sub(center);d.applyAxisAngle(new T.Vector3(0,1,0),action==="left"?-.3:.3);camera.position.copy(center).add(d);}
        else if(action==="in"||action==="out")camera.position.sub(center).multiplyScalar(action==="in"?.8:1.25).add(center);
        else{center.set(0,y,0);camera.position.set(action==="top"?0:span*.9,action==="top"?span*1.8:action==="side"?y:span*.5,action==="top"?.01:span*1.25);}
        controls.update();render();
      };
      const update=(v:Settings)=>{volumeGroup.scale.y=v.scale;logGroup.scale.y=v.scale;logGroup.visible=v.logs;planePaint.opacity=v.surface*(surfaceTexture?1:.15);waters.forEach(m=>{m.opacity=v.water;});render();};
      const setSurface=(image:HTMLCanvasElement|null)=>{
        surfaceTexture?.dispose();surfaceTexture=image?new T.CanvasTexture(image):null;
        if(surfaceTexture)surfaceTexture.colorSpace=T.SRGBColorSpace;
        planePaint.map=surfaceTexture;planePaint.color.set(image?"#ffffff":"#83a4a7");planePaint.needsUpdate=true;
        update(values.current);
      };
      api.current={camera:orient,update,setSurface};setSurface(snapshotRef.current?.volume===volume?snapshotRef.current.image:null);orient("reset");
      const resize=()=>{if(!host.current)return;const w=Math.max(1,host.current.clientWidth),h=w<600?340:450;renderer.setSize(w,h);camera.aspect=w/h;camera.updateProjectionMatrix();render();};
      const ray=new T.Raycaster(),point=new T.Vector2();let down=[0,0];
      const pointerDown=(e:PointerEvent)=>{down=[e.clientX,e.clientY];};
      const pointerUp=(e:PointerEvent)=>{if(Math.hypot(e.clientX-down[0],e.clientY-down[1])>5)return;const b=renderer.domElement.getBoundingClientRect();point.set((e.clientX-b.left)/b.width*2-1,-(e.clientY-b.top)/b.height*2+1);ray.setFromCamera(point,camera);
        const hit=ray.intersectObjects(pickable.filter(m=>m.userData.record?values.current.logs:values.current.water>0))[0];if(!hit)return;
        if(hit.object.userData.record)inspectRef.current(hit.object.userData.record,hit.object.userData.interval);else setSelection(hit.object.userData.envelope.id);
      };
      const lost=(e:Event)=>{e.preventDefault();setFailure("3D interrupted. The 2D locator and source ranges remain available below.");};
      renderer.domElement.addEventListener("pointerdown",pointerDown);renderer.domElement.addEventListener("pointerup",pointerUp);renderer.domElement.addEventListener("webglcontextlost",lost);controls.addEventListener("change",render);document.addEventListener("visibilitychange",render);
      const observer=new ResizeObserver(resize);observer.observe(host.current);resize();const disposeResources=cleanup;
      cleanup=()=>{observer.disconnect();controls.removeEventListener("change",render);document.removeEventListener("visibilitychange",render);renderer.domElement.removeEventListener("pointerdown",pointerDown);renderer.domElement.removeEventListener("pointerup",pointerUp);renderer.domElement.removeEventListener("webglcontextlost",lost);disposeResources();};
    }).catch(()=>{cleanup?.();cleanup=undefined;if(!disposed)setFailure("Aquifer 3D is unavailable on this device. Read the source ranges below and continue on the 2D locator.");});
    return()=>{disposed=true;api.current=null;cleanup?.();};
  },[volume,records]);
  useEffect(()=>{api.current?.setSurface(snapshot?.image??null);},[snapshot?.image]);
  useEffect(()=>{api.current?.update(values.current);},[surface,water,scale,logs]);
  const selected=snapshot?.volume.envelopes.find(e=>e.id===selection);
  return <section className={s.materialExplorer} aria-label="Aquifer shape from source ranges">
    <header className={s.materialHeading}><div><span>HIGH PLAINS · 2022–2024</span><h3>Aquifer envelope beneath the locator</h3></div><a href={KGS_ATLAS_URL} target="_blank" rel="noreferrer">KGS Atlas ↗</a></header>
    <div className={s.modelControls}><button type="button" onClick={()=>{setFailure("");setRetry(v=>v+1);}}>Refresh from locator</button><button type="button" onClick={()=>{onFlatMap();onLocate([-100.5,38.5]);}}>High Plains example</button></div>
    <p role="status">{status}</p><p className={s.muted} role="status">{surfaceStatus}</p>{failure&&<p role="alert">{failure}</p>}
    {snapshot&&<div className={s.modelStage}><div ref={host} hidden={!!failure} /><div className={s.modelStamp}>2022–2024 SOURCE RANGES · {scale}× vertical<br />{snapshot.image?"Captured surface map":"Locator extent · surface image unavailable"} · depth below local ground</div></div>}
    <p className={s.modelBoundary}>Blue is a possible depth envelope from regional source ranges—not a water-filled cavern or exact reservoir. The map plane stays above it as you orbit. Depth is below a flattened local-ground reference, not a shared elevation datum.</p>
    <div className={s.modelControls}>
      <label>Surface map <input type="range" min="0" max="100" value={surface*100} onChange={e=>setSurface(Number(e.target.value)/100)} />{Math.round(surface*100)}%</label>
      <label>Aquifer opacity <input type="range" min="0" max="100" value={water*100} onChange={e=>setWater(Number(e.target.value)/100)} />{Math.round(water*100)}%</label>
      <label>Vertical display <select value={scale} onChange={e=>setScale(Number(e.target.value))}>{[1,10,25,50,100,250,500].map(n=><option key={n} value={n}>{n}×</option>)}</select></label><button type="button" aria-pressed={logs} onClick={()=>setLogs(v=>!v)}>Show loaded logs</button>
    </div>
    <div className={s.modelCamera} aria-label="Aquifer camera controls">{([['reset','Reset view'],['top','Top'],['side','Side'],['left','Rotate left'],['right','Rotate right'],['in','Zoom in'],['out','Zoom out']] as const).map(([action,label])=><button type="button" key={action} disabled={!snapshot||!!failure} onClick={()=>api.current?.camera(action)}>{label}</button>)}</div>

    {snapshot&&<>
      <p className={s.muted}>Captured locator extent: {snapshot.volume.bounds.map(n=>n.toFixed(4)).join(", ")}. Loaded logs use approximate recorded coordinates and individual depth references; no seams connect them. Up to 50 records / 400 intervals, clipped 50 m below the deepest aquifer envelope (500 m if no envelope). These are record-depth diagrams, not verified vertical trajectories. The overlaid logs follow the well/core record timeline. The aquifer shape stays fixed to its 2022–2024 source period; the record timeline does not animate historical water occupancy.</p>
      {!snapshot.volume.envelopes.length&&<p>No bounded aquifer overlap is available in this view. Try the High Plains example. Missing or open-ended classes are not drawn.</p>}
      {selected&&<p className={s.selectedLayer}>Selected region: water-table depth {selected.depthFeet.join("–")} ft; saturated thickness {selected.thicknessFeet.join("–")} ft. Possible outer depth envelope {selected.shallowMeters.toFixed(1)}–{selected.deepMeters.toFixed(1)} m. This range does not mean the whole envelope is saturated.</p>}
      <details><summary>Inspect source ranges and limits</summary><div className={s.materialLegend}>{snapshot.volume.envelopes.map(e=><button type="button" key={e.id} aria-pressed={selection===e.id} onClick={()=>setSelection(e.id)}>Depth {e.depthFeet.join("–")} ft · thickness {e.thicknessFeet.join("–")} ft</button>)}</div><p>Derived by intersecting KGS classified depth-to-water and saturated-thickness polygons from the same 2022–2024 period. No class midpoint, precise bedrock surface, stored water volume, flow, ownership or extraction suitability is asserted. Open-ended classes and missing values are withheld. Original geometry was generalized to 0.0005 degrees. Historical numerical surfaces and additional aquifers need separate qualification.</p></details>
    </>}
  </section>;
}
