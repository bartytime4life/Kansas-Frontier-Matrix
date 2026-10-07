"use client";
import { useEffect, useMemo, useRef, useState } from "react";
import type { Map as MapLibreMap } from "./maplibre-seam";
import { startAquiferVolumeWorker } from "./subsurface-workers";
import { projectVolumePosition, volumeDepthScale } from "./aquifer-volume";
import { materialFor, materialInfo } from "./subsurface-materials";
import { type Borehole, type DepthInterval } from "./subsurface-model";
import { cutawayCameraFit, cutawayRecords, pickCutawaySource } from "./cutaway-model";
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
  const [surface,setSurface]=useState(.82),[water,setWater]=useState(.22),[scale,setScale]=useState(25),[logs,setLogs]=useState(true);
  const [failure,setFailure]=useState(""),[selection,setSelection]=useState<string|null>(null);
  const [pickedLog,setPickedLog]=useState<{label:string;recordId:string}|null>(null);
  const host=useRef<HTMLDivElement>(null),api=useRef<{camera:(action:CameraAction)=>void;update:(v:Settings)=>void;setSurface:(image:HTMLCanvasElement|null)=>void;highlightRecord:(id:string|null)=>void}|null>(null);
  const values=useRef<Settings>({surface,water,scale,logs});
  const inspectRef=useRef(onInspect);
  const snapshotRef=useRef(snapshot);
  const volume=snapshot?.volume;
  const drawn = useMemo(() => volume ? cutawayRecords(volume, records) : null, [volume, records]);
  useEffect(()=>{values.current={surface,water,scale,logs};},[surface,water,scale,logs]);
  useEffect(()=>{inspectRef.current=onInspect;},[onInspect]);
  useEffect(()=>{snapshotRef.current=snapshot;},[snapshot]);
  useEffect(()=>{let cancelled=false;queueMicrotask(()=>{if(!cancelled){setSelection(null);setPickedLog(null);}});return()=>{cancelled=true;};},[volume,records]);
  useEffect(()=>{
    if(!map)return;
    let cancelled=false;
    let worker:Worker;
    try{worker=startAquiferVolumeWorker();}catch{queueMicrotask(()=>{if(!cancelled)setStatus("Aquifer preparation worker unavailable. The locator and logs remain usable.");});return()=>{cancelled=true;};}
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
      renderer.domElement.tabIndex=0;renderer.domElement.setAttribute("aria-label","3D cutaway of independent well logs and aquifer source ranges below a flat locator map. Drag to orbit; camera buttons and source lists provide keyboard alternatives.");host.current.append(renderer.domElement);
      const scene=new T.Scene();scene.background=new T.Color("#101b20");const camera=new T.PerspectiveCamera(40,1,.01,500);
      const controls=new OrbitControls(camera,renderer.domElement);controls.enableDamping=false;controls.minDistance=.02;controls.maxPolarAngle=Math.PI*.92;resources.push(controls);
      const bounds=volume.bounds,k=volumeDepthScale(bounds);
      const north=projectVolumePosition(bounds[0],bounds[3],bounds).z,south=projectVolumePosition(bounds[0],bounds[1],bounds).z;
      const planeGeometry=new T.PlaneGeometry(6,south-north);planeGeometry.rotateX(-Math.PI/2);resources.push(planeGeometry);
      const planePaint=new T.MeshBasicMaterial({color:"#697d77",transparent:true,opacity:values.current.surface*.15,side:T.DoubleSide,depthWrite:false});resources.push(planePaint);
      let surfaceTexture:InstanceType<typeof T.CanvasTexture>|null=null;
      resources.push({dispose:()=>surfaceTexture?.dispose()});
      const plane=new T.Mesh(planeGeometry,planePaint);plane.position.y=.0005;plane.renderOrder=3;scene.add(plane);
      const borderGeom=new T.EdgesGeometry(planeGeometry),borderPaint=new T.LineBasicMaterial({color:"#d2ad75"});resources.push(borderGeom,borderPaint);const border=new T.LineSegments(borderGeom,borderPaint);border.position.y=.001;scene.add(border);
      const volumeGroup=new T.Group(),logGroup=new T.Group();scene.add(volumeGroup,logGroup);
      const waters:InstanceType<typeof T.MeshStandardMaterial>[]=[],pickable:InstanceType<typeof T.Mesh>[]=[];
      for(const {envelope,geometry} of aquiferGeometries(T,volume)){
        resources.push(geometry);
        const paint=new T.MeshStandardMaterial({color:"#238da9",roughness:.65,metalness:0,transparent:true,opacity:values.current.water,depthWrite:false,side:T.DoubleSide});waters.push(paint);resources.push(paint);
        const mesh=new T.Mesh(geometry,paint);mesh.userData.envelope=envelope;mesh.renderOrder=1;volumeGroup.add(mesh);pickable.push(mesh);
      }
      const plotted=cutawayRecords(volume,records), deepest=plotted.deepest;
      const frameGroup=new T.Group();scene.add(frameGroup);
      // Dark back walls describe the inspection extent, never a lithology class.
      const frameDepth=deepest*k;
      const wallPaint=new T.MeshBasicMaterial({color:"#172328",side:T.DoubleSide});resources.push(wallPaint);
      for(const face of ["back","left","floor"] as const){
        const geometry=new T.PlaneGeometry(face==="left"?south-north:6,face==="floor"?south-north:frameDepth);resources.push(geometry);
        const mesh=new T.Mesh(geometry,wallPaint);
        if(face==="floor"){mesh.rotation.x=-Math.PI/2;mesh.position.y=-frameDepth;}
        else if(face==="left"){mesh.rotation.y=Math.PI/2;mesh.position.set(-3,-frameDepth/2,0);}
        else mesh.position.set(0,-frameDepth/2,north);
        frameGroup.add(mesh);
      }
      const framePoints:number[]=[];
      const segment=(a:number[],b:number[])=>framePoints.push(...a,...b);
      for(const x of [-3,3])for(const z of [north,south])segment([x,0,z],[x,-frameDepth,z]);
      for(const y of [0,-frameDepth]){
        segment([-3,y,north],[3,y,north]);segment([-3,y,south],[3,y,south]);
        segment([-3,y,north],[-3,y,south]);segment([3,y,north],[3,y,south]);
      }
      const frameGeometry=new T.BufferGeometry();frameGeometry.setAttribute("position",new T.Float32BufferAttribute(framePoints,3));
      const framePaint=new T.LineBasicMaterial({color:"#b28a5e",transparent:true,opacity:.65});resources.push(frameGeometry,framePaint);
      frameGroup.add(new T.LineSegments(frameGeometry,framePaint));
      const guides:number[]=[];
      for(const f of [.25,.5,.75]){guides.push(-3,-frameDepth*f,north,3,-frameDepth*f,north,-3,-frameDepth*f,north,-3,-frameDepth*f,south);}
      const guideGeometry=new T.BufferGeometry();guideGeometry.setAttribute("position",new T.Float32BufferAttribute(guides,3));
      const guidePaint=new T.LineBasicMaterial({color:"#698082",transparent:true,opacity:.25});resources.push(guideGeometry,guidePaint);frameGroup.add(new T.LineSegments(guideGeometry,guidePaint));
      const tickSprites:{sprite:InstanceType<typeof T.Sprite>;fraction:number}[]=[];
      for(const fraction of [0,.25,.5,.75,1]){
        const label=document.createElement("canvas");label.width=180;label.height=48;
        const ctx=label.getContext("2d");if(!ctx)continue;
        ctx.fillStyle="#101b20";ctx.fillRect(0,0,180,48);ctx.font="28px monospace";ctx.fillStyle="#eee5cf";ctx.textAlign="right";ctx.fillText(`${(deepest*fraction).toFixed(0)} m`,168,34);
        const texture=new T.CanvasTexture(label);texture.colorSpace=T.SRGBColorSpace;
        const paint=new T.SpriteMaterial({map:texture,transparent:true,depthTest:false});resources.push(texture,paint);
        const sprite=new T.Sprite(paint);sprite.scale.set(.72,.18,1);scene.add(sprite);tickSprites.push({sprite,fraction});
      }
      const collars=new Set<string>();
      const diagramColumns:{mesh:InstanceType<typeof T.Mesh>;edge:InstanceType<typeof T.LineSegments>;edgePaint:InstanceType<typeof T.LineBasicMaterial>;recordId:string}[]=[];
      let highlightedRecord:string|null=null;
      for(const {record,interval,top,bottom} of plotted.intervals){
        const p=projectVolumePosition(...record.coordinates,bounds);
        const geometry=new T.CylinderGeometry(.5,.5,(bottom-top)*k,12),paint=new T.MeshBasicMaterial({color:materialInfo(materialFor(interval,record.kind)).color});resources.push(geometry,paint);
        const mesh=new T.Mesh(geometry,paint);mesh.position.set(p.x,-(top+bottom)/2*k,p.z);mesh.userData.record=record;mesh.userData.interval=interval;mesh.renderOrder=4;logGroup.add(mesh);pickable.push(mesh);
        const edgeGeometry=new T.EdgesGeometry(geometry,50),edgePaint=new T.LineBasicMaterial({color:"#c9c3af",transparent:true,opacity:.65});resources.push(edgeGeometry,edgePaint);
        const edge=new T.LineSegments(edgeGeometry,edgePaint);edge.renderOrder=5;mesh.add(edge);diagramColumns.push({mesh,edge,edgePaint,recordId:record.id});
        if(!collars.has(record.id)){
          collars.add(record.id);const collarGeometry=new T.RingGeometry(.03,.047,16);collarGeometry.rotateX(-Math.PI/2);
          const collarPaint=new T.MeshBasicMaterial({color:record.kind==="core"?"#baa2df":"#e0b46f",side:T.DoubleSide});resources.push(collarGeometry,collarPaint);
          const collar=new T.Mesh(collarGeometry,collarPaint);collar.position.set(p.x,.004,p.z);collar.userData.record=record;logGroup.add(collar);pickable.push(collar);
        }
      }
      scene.add(new T.HemisphereLight(0xd2eeff,0x194955,2.5));const light=new T.DirectionalLight(0xffffff,2);light.position.set(4,6,3);scene.add(light);
      const worldPosition=new T.Vector3(),cameraSpace=new T.Vector3();
      const worldPerPixel=(object:InstanceType<typeof T.Object3D>)=>{
        object.getWorldPosition(worldPosition);cameraSpace.copy(worldPosition).applyMatrix4(camera.matrixWorldInverse);
        return 2*Math.max(camera.near,Math.abs(cameraSpace.z))*Math.tan(T.MathUtils.degToRad(camera.fov)/2)/Math.max(1,renderer.domElement.clientHeight);
      };
      const render=()=>{
        if(disposed||document.hidden)return;
        scene.updateMatrixWorld(true);camera.updateMatrixWorld(true);
        // Screen-legible diagram widths, never a claim about physical well diameter.
        for(const {mesh,edgePaint,recordId} of diagramColumns){
          const chosen=recordId===highlightedRecord,diameter=worldPerPixel(mesh)*(chosen?11:9);
          mesh.scale.x=diameter;mesh.scale.z=diameter;
          edgePaint.color.set(chosen?"#ffe2a3":"#c9c3af");edgePaint.opacity=chosen?1:.65;
        }
        const tickTop=tickSprites[0]?.sprite.position.clone().project(camera),tickBottom=tickSprites.at(-1)?.sprite.position.clone().project(camera);
        const tickPixels=tickTop&&tickBottom?Math.abs(tickTop.y-tickBottom.y)*renderer.domElement.clientHeight/2:0;
        for(const {sprite,fraction} of tickSprites){
          const pixel=worldPerPixel(sprite);sprite.scale.set(pixel*90,pixel*24,1);
          sprite.visible=fraction===1||(fraction===0&&tickPixels>=30)||(fraction===.5&&tickPixels>=66)||(fraction!==0&&fraction!==.5&&tickPixels>=120);
        }
        renderer.render(scene,camera);
      };
      const fit=(direction:readonly [number,number,number])=>cutawayCameraFit(6,south-north,deepest*k*values.current.scale,camera.aspect,direction,renderer.domElement.clientHeight);
      const orient=(action:CameraAction)=>{
        const direction:readonly [number,number,number]=action==="top"?[0,1,.001]:action==="side"?[.2,0,1]:[.55,.6,1];
        const center=controls.target,y=-deepest*k*values.current.scale/2,{distance,near,far,offsetX,offsetY}=fit(direction);
        if(action==="reset"||action==="top"||action==="side"){const w=renderer.domElement.clientWidth,h=renderer.domElement.clientHeight;camera.setViewOffset(w,h,offsetX*w/2,-offsetY*h/2,w,h);}
        controls.maxDistance=distance*8;camera.near=near;camera.far=far;camera.updateProjectionMatrix();
        if(action==="left"||action==="right"){const d=camera.position.clone().sub(center);d.applyAxisAngle(new T.Vector3(0,1,0),action==="left"?-.3:.3);camera.position.copy(center).add(d);}
        else if(action==="in"||action==="out")camera.position.sub(center).multiplyScalar(action==="in"?.8:1.25).add(center);
        else{center.set(0,y,0);camera.position.copy(center).add(new T.Vector3(...direction).normalize().multiplyScalar(distance));}
        controls.update();render();
      };
      let lastScale=values.current.scale;
      const update=(v:Settings)=>{
        volumeGroup.scale.y=v.scale;logGroup.scale.y=v.scale;frameGroup.scale.y=v.scale;logGroup.visible=v.logs;
        tickSprites.forEach(({sprite,fraction})=>sprite.position.set(-3.42,-frameDepth*fraction*v.scale,south));
        planePaint.opacity=v.surface*(surfaceTexture?1:.15);waters.forEach(m=>{m.opacity=v.water;});
        if(lastScale!==v.scale){lastScale=v.scale;orient("reset");}else render();
      };
      const setSurface=(image:HTMLCanvasElement|null)=>{
        surfaceTexture?.dispose();surfaceTexture=image?new T.CanvasTexture(image):null;
        if(surfaceTexture)surfaceTexture.colorSpace=T.SRGBColorSpace;
        planePaint.map=surfaceTexture;planePaint.color.set(image?"#ffffff":"#83a4a7");planePaint.needsUpdate=true;
        update(values.current);
      };
      api.current={camera:orient,update,setSurface,highlightRecord:(id)=>{highlightedRecord=id;render();}};setSurface(snapshotRef.current?.volume===volume?snapshotRef.current.image:null);orient("reset");
      const resize=()=>{if(!host.current)return;const w=Math.max(1,host.current.clientWidth),h=Math.max(1,host.current.clientHeight);renderer.setSize(w,h);camera.aspect=w/h;camera.updateProjectionMatrix();orient("reset");};
      const ray=new T.Raycaster(),point=new T.Vector2();let down=[0,0];
      const pointerDown=(e:PointerEvent)=>{down=[e.clientX,e.clientY];};
      const pointerUp=(e:PointerEvent)=>{if(Math.hypot(e.clientX-down[0],e.clientY-down[1])>5)return;const b=renderer.domElement.getBoundingClientRect();point.set((e.clientX-b.left)/b.width*2-1,-(e.clientY-b.top)/b.height*2+1);ray.setFromCamera(point,camera);
        const hit=pickCutawaySource(ray,pickable.filter(m=>m.userData.record?values.current.logs:values.current.water>0));if(!hit)return;
        if(hit.object.userData.record){const r=hit.object.userData.record as Borehole,i=hit.object.userData.interval as DepthInterval|undefined;setSelection(null);setPickedLog({recordId:r.id,label:`${r.name}${i?` · ${i.top}–${i.bottom} ${r.depthUnit}: ${i.description}`:""}`});inspectRef.current(r,i);}else{setPickedLog(null);setSelection(hit.object.userData.envelope.id);}
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
  useEffect(()=>{api.current?.highlightRecord(pickedLog?.recordId??null);},[pickedLog]);
  const selected=snapshot?.volume.envelopes.find(e=>e.id===selection);
  const focusHere=()=>{const center=map?.getCenter();if(center){onFlatMap();onLocate([center.lng,center.lat]);}};
  return <section className={s.cutawayExplorer} aria-label="3D cutaway from source records">
    <div className={s.cutawayHeading}>
      <div><span className={s.cutawayEyebrow}>KANSAS / BELOW THE SURFACE</span><h3>Read the ground.</h3></div>
      <div className={s.cutawayEntryActions}><button type="button" onClick={focusHere}>Explore this area <span aria-hidden="true">↗</span></button><button type="button" onClick={()=>{onFlatMap();onLocate([-100.5,38.5]);}}>High Plains example</button></div>
    </div>
    <div className={s.cutawayWorkspace}>
      <div className={s.cutawayStage}>
        <div ref={host} className={s.cutawayCanvas} hidden={!snapshot||!!failure} />
        {!snapshot&&!failure&&<div className={s.cutawayEmpty}><span className={s.cutawayEyebrow}>A CLOSER LOOK</span><h4>Choose a piece of Kansas.</h4><p>Explore a local area to reveal recorded well columns and available aquifer ranges beneath the map.</p><button type="button" onClick={focusHere}>Explore this area</button><p className={s.cutawayEmptyStatus} role="status">{status}</p></div>}
        {failure&&<div className={s.cutawayEmpty}><h4>Continue with the source records.</h4><p role="alert">{failure}</p><button type="button" onClick={()=>{setFailure("");setRetry(v=>v+1);}}>Retry 3D view</button></div>}
        <div className={s.cutawayCompass} aria-label="The locator is north-up; the 3D view can orbit"><span>LOCATOR N</span><i aria-hidden="true">↑</i></div>
        <div className={s.cutawaySceneLabel}><span className={s.cutawayEyebrow}>FLAT LOCAL-GROUND REFERENCE</span><strong>Independent records. Open questions.</strong><span>Dark space is unobserved · no continuous geology inferred</span></div>
        <div className={s.cutawayCamera} aria-label="Cutaway camera controls">{([['reset','Reset view'],['top','Top'],['side','Side'],['left','↶'],['right','↷'],['in','+'],['out','−']] as const).map(([action,label])=><button type="button" key={action} aria-label={action==='left'?'Rotate left':action==='right'?'Rotate right':action==='in'?'Zoom in':action==='out'?'Zoom out':label} disabled={!snapshot||!!failure} onClick={()=>api.current?.camera(action)}>{label}</button>)}</div>
        <div className={s.cutawayStamp}>{scale}× VERTICAL <span>·</span> {snapshot?.image?"CAPTURED LOCATOR":"LOCATOR IMAGE UNAVAILABLE"}</div>
      </div>
      <aside className={s.cutawayConsole} aria-label="Cutaway appearance and evidence">
        <div className={s.cutawayConsoleTitle}><span>VIEW SETTINGS</span><span aria-hidden="true">◈</span></div>
        <label className={s.cutawayRange}>Surface map <output>{Math.round(surface*100)}%</output><input aria-label="Surface map opacity" type="range" min="0" max="100" value={surface*100} onChange={e=>setSurface(Number(e.target.value)/100)} /></label>
        <label className={s.cutawayRange}>Aquifer range <output>{Math.round(water*100)}%</output><input aria-label="Aquifer opacity" type="range" min="0" max="100" value={water*100} onChange={e=>setWater(Number(e.target.value)/100)} /></label>
        <label className={s.cutawayScale}>Vertical scale <select aria-label="Cutaway vertical scale" value={scale} onChange={e=>setScale(Number(e.target.value))}>{[1,10,25,50,100,250,500].map(n=><option key={n} value={n}>{n}×</option>)}</select></label>
        <button className={s.cutawayLogToggle} type="button" aria-pressed={logs} onClick={()=>setLogs(v=>!v)}><span aria-hidden="true">{logs?"☑":"☐"}</span> Recorded columns <b>{drawn?.recordCount??0}</b></button>
        <div className={s.cutawayLegend}><span><i data-kind="log"/>Log descriptions · width illustrative</span><span><i data-kind="core"/>Core inventory envelopes</span><span><i data-kind="aquifer"/>Aquifer uncertainty · 2022–2024</span><span><i data-kind="unknown"/>Unobserved / unlogged</span></div>
        <p className={s.cutawayCaution}>Depths use each record’s own recorded depth reference. The flat map is not surveyed terrain. Choose imagery through Map → Basemap.</p>
        <details className={s.cutawayEvidence}><summary>Evidence &amp; source bounds <span>{snapshot?.volume.envelopes.length??0} ranges</span></summary>
          <p role="status">{status}</p><p role="status">{surfaceStatus}</p>
          <p>Blue shows possible outer depth ranges, not a filled reservoir. Classified depth-to-water and saturated-thickness polygons retain their original bounds and holes. No midpoint, cave, flow, or water volume is inferred.</p>
          {snapshot&&<><p>{drawn?.recordCount} records / {drawn?.intervals.length} intervals in this extent. Up to 50 records / 400 intervals; depth clipping at {drawn?.limit.toFixed(1)} m{drawn?.clipped?" (some intervals clipped)":""}. Columns are diagrams, not verified trajectories. No seams connect them.</p><p>Extent: {snapshot.volume.bounds.map(n=>n.toFixed(4)).join(", ")}. Original polygon generalization: 0.0005°.</p>{!snapshot.volume.envelopes.length&&<p>No bounded aquifer overlap here. Missing and open-ended classes remain withheld.</p>}<div className={s.cutawaySourceList}>{snapshot.volume.envelopes.map(e=><button type="button" key={e.id} aria-pressed={selection===e.id} onClick={()=>{setPickedLog(null);setSelection(e.id);}}>Depth {e.depthFeet.join("–")} ft · thickness {e.thicknessFeet.join("–")} ft</button>)}</div></>}
          <a href={KGS_ATLAS_URL} target="_blank" rel="noreferrer">Read the KGS Atlas ↗</a><button type="button" onClick={()=>{setFailure("");setRetry(v=>v+1);}}>Refresh from locator</button>
        </details>
      </aside>
    </div>
    <div className={s.cutawayReadout} aria-live="polite"><span className={s.cutawayEyebrow}>INSPECT</span>{pickedLog?<span>{pickedLog.label}</span>:selected?<span>Water-table depth {selected.depthFeet.join("–")} ft · thickness {selected.thicknessFeet.join("–")} ft · possible outer envelope {selected.shallowMeters.toFixed(1)}–{selected.deepMeters.toFixed(1)} m. Not wholly saturated.</span>:<span>{snapshot?"Drag to orbit · select a column or blue range to inspect its source.":"Use Explore this area or High Plains example to prepare a bounded local view."}</span>}</div>
  </section>;
}
