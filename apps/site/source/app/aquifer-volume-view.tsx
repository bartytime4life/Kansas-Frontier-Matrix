"use client";
import { useEffect, useMemo, useRef, useState, type ReactNode } from "react";
import type { Map as MapLibreMap } from "./maplibre-seam";
import { startAquiferVolumeWorker } from "./subsurface-workers";
import { projectVolumePosition, volumeDepthScale, validVolumeBounds } from "./aquifer-volume";
import { materialFor, materialInfo } from "./subsurface-materials";
import { type Borehole, type DepthInterval } from "./subsurface-model";
import { cutawayCameraFit, cutawayRecords, pickCutawaySource } from "./cutaway-model";
import { bindCameraKeyboardInterruption, createCutawayCameraMotion, rotateCutawayCamera, type CameraPose } from "./cutaway-camera";
import { KGS_ATLAS_URL } from "./aquifer-layers";
import s from "./subsurface.module.css";
import { aquiferGeometries } from "./aquifer-volume-mesh";
import { startAquiferView, locatorBounds, type AquiferViewSnapshot } from "./aquifer-view-session";
type VolumeBounds = [number,number,number,number];
type Snapshot = AquiferViewSnapshot<HTMLCanvasElement>;
type CameraAction="reset"|"top"|"side"|"left"|"right"|"in"|"out";
type Settings={surface:number;water:number;scale:number;logs:boolean;smooth:boolean;navigation:"orbit"|"pan"};
export default function AquiferVolumeView({active=true,map,records,onFlatMap,onInspect,onLocatorSlot,sliceEntry,onArea,recordsLoading,recordStatus,partial,recordNavigation,recordsAvailable,onResetRecords}:{active?:boolean;map:MapLibreMap|null;records:Borehole[];onFlatMap:()=>void;onLocate:(point:[number,number],retainView?:boolean)=>void;onInspect:(record:Borehole,interval?:DepthInterval)=>void;locator:{anchor:[number,number];pinned:boolean};onLocatorSlot:(slot:HTMLDivElement|null)=>void;sliceEntry?:ReactNode;onArea:(bounds:VolumeBounds|null)=>void;recordsLoading:boolean;recordStatus:string;partial:boolean;recordNavigation:ReactNode;recordsAvailable:number;onResetRecords:()=>void}){
  const [snapshot,setSnapshot]=useState<Snapshot|null>(null),[status,setStatus]=useState("Preparing the current locator area…"),[retry,setRetry]=useState(0);
  const [surfaceStatus,setSurfaceStatus]=useState(""),[previewChanged,setPreviewChanged]=useState(false);
  const [frame,setFrame]=useState<VolumeBounds|null>(null);
  const modelFocus=useRef<HTMLElement|null>(null),focusAfterApply=useRef(false);
  const [navigation,setNavigation]=useState<"orbit"|"pan">("orbit");
  const areaSession=useRef<{prepare:()=>void}|null>(null),onAreaRef=useRef(onArea);
  useEffect(()=>{onAreaRef.current=onArea;},[onArea]);
  const [surface,setSurface]=useState(.82),[water,setWater]=useState(.22),[scale,setScale]=useState(25),[logs,setLogs]=useState(true),[smooth,setSmooth]=useState(true);
  const [failure,setFailure]=useState(""),[selection,setSelection]=useState<string|null>(null);
  const [pickedLog,setPickedLog]=useState<{label:string;recordId:string}|null>(null);
  const host=useRef<HTMLDivElement>(null),api=useRef<{camera:(action:CameraAction)=>void;update:(v:Settings)=>void;setSurface:(image:HTMLCanvasElement|null)=>void;highlightRecord:(id:string|null)=>void}|null>(null);
  const values=useRef<Settings>({surface,water,scale,logs,smooth,navigation});
  const inspectRef=useRef(onInspect);
  const snapshotRef=useRef(snapshot);
  const pickedLogRef=useRef(pickedLog);
  const cameraMemory=useRef<{area:string;pose:CameraPose;awaitingRecords:boolean;awaitingAquifer:boolean;interacted:boolean}|null>(null);
  const volume=snapshot?.volume;
  const aquiferLoading=snapshot?.aquiferState==="loading";
  useEffect(()=>{if(!map)return;const read=()=>{try{setFrame(locatorBounds(map));}catch{setFrame(null);}};read();map.on("moveend",read);map.on("resize",read);map.on("load",read);return()=>{map.off("moveend",read);map.off("resize",read);map.off("load",read);};},[map]);
  useEffect(()=>{if(volume&&focusAfterApply.current){focusAfterApply.current=false;modelFocus.current?.focus({preventScroll:false});}},[volume]);
  const drawn = useMemo(() => volume ? cutawayRecords(volume, records) : null, [volume, records]);
  const sceneRenderable=Boolean(volume&&(recordsLoading||aquiferLoading||drawn?.recordCount||volume.envelopes.length));
  useEffect(()=>{values.current={surface,water,scale,logs,smooth,navigation};},[surface,water,scale,logs,smooth,navigation]);
  useEffect(()=>{inspectRef.current=onInspect;},[onInspect]);
  useEffect(()=>{snapshotRef.current=snapshot;},[snapshot]);
  useEffect(()=>{pickedLogRef.current=pickedLog;},[pickedLog]);
  useEffect(()=>{let cancelled=false;queueMicrotask(()=>{if(cancelled)return;setSelection(id=>volume?.envelopes.some(e=>e.id===id)?id:null);setPickedLog(pick=>pick&&drawn?.intervals.some(i=>i.record.id===pick.recordId)?pick:null);});return()=>{cancelled=true;};},[volume,drawn]);
  useEffect(()=>{
    if(!map||!active)return;
    let worker:Worker|null=null;
    try{worker=startAquiferVolumeWorker();}catch{ /* Independent record loading still gets an applied frame. */ }
    const stop=startAquiferView<HTMLCanvasElement>({map,worker,manual:true,initialSnapshot:snapshotRef.current,onArea:bounds=>onAreaRef.current(bounds),onPreview:setPreviewChanged,onSnapshot:setSnapshot,onStatus:setStatus,onSurfaceStatus:setSurfaceStatus,sampleSurface:()=>{
      const source=map.getCanvas(),image=document.createElement("canvas");
      const ratio=Math.min(1,1024/Math.max(source.width,source.height));image.width=Math.max(1,Math.round(source.width*ratio));image.height=Math.max(1,Math.round(source.height*ratio));
      const ctx=image.getContext("2d");if(!ctx)throw new Error("Surface capture unavailable");
      ctx.drawImage(source,0,0,image.width,image.height);
      // Only read back a complete frame; failure does not hold aquifer geometry.
      ctx.getImageData(0,0,1,1);return image;
    }});
    areaSession.current=stop;
    return()=>{areaSession.current=null;stop();worker?.terminate();};
  },[map,retry,active]);

  useEffect(()=>{
    if(!active||!sceneRenderable||!volume||!host.current)return;
    setFailure("");
    let disposed=false,cleanup:(()=>void)|undefined;
    void Promise.all([import("three"),import("three/addons/controls/OrbitControls.js")]).then(([T,{OrbitControls}])=>{
      if(disposed||!host.current)return;
      const renderer=new T.WebGLRenderer({antialias:true});renderer.setPixelRatio(Math.min(devicePixelRatio,1.5));
      const resources:{dispose:()=>void}[]=[];cleanup=()=>{resources.forEach(r=>r.dispose());renderer.dispose();renderer.domElement.remove();};
      renderer.domElement.tabIndex=0;renderer.domElement.setAttribute("aria-label","3D cutaway of independent well logs and aquifer source ranges below a flat locator map. Drag to orbit or choose Move to pan; arrows pan, modified arrows rotate, and buttons provide alternatives.");host.current.append(renderer.domElement);
      const scene=new T.Scene();scene.background=new T.Color("#101b20");const camera=new T.PerspectiveCamera(40,1,.01,500);
      const controls=new OrbitControls(camera,renderer.domElement),motionPreference=matchMedia("(prefers-reduced-motion: reduce)");
      controls.enableDamping=!motionPreference.matches;controls.dampingFactor=.14;controls.minDistance=.02;controls.maxPolarAngle=Math.PI*.92;controls.zoomToCursor=true;controls.listenToKeyEvents(renderer.domElement);resources.push(controls);
      const bounds=volume.bounds,k=volumeDepthScale(bounds),area=bounds.join(",");
      const previousCamera=cameraMemory.current?.area===area?cameraMemory.current:null;
      let awaitingRecords=previousCamera?.awaitingRecords??recordsLoading,awaitingAquifer=previousCamera?.awaitingAquifer??aquiferLoading,interacted=previousCamera?.interacted??false;
      const fitFirstEvidence=!interacted&&((awaitingRecords&&!recordsLoading)||(awaitingAquifer&&!aquiferLoading));
      if(!recordsLoading)awaitingRecords=false;
      if(!aquiferLoading)awaitingAquifer=false;
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
      let highlightedRecord:string|null=pickedLogRef.current?.recordId??null;
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
      let viewOffset:[number,number]=[0,0],dampingFrame:number|null=null;
      const readPose=():CameraPose=>({position:camera.position.toArray(),target:controls.target.toArray(),offset:[...viewOffset]});
      const applyPose=(pose:CameraPose)=>{
        camera.position.fromArray(pose.position);controls.target.fromArray(pose.target);viewOffset=[...pose.offset];
        const w=Math.max(1,renderer.domElement.clientWidth),h=Math.max(1,renderer.domElement.clientHeight);
        camera.setViewOffset(w,h,viewOffset[0]*w/2,-viewOffset[1]*h/2,w,h);
        const distance=camera.position.distanceTo(controls.target),extent=Math.max(6,south-north,deepest*k*values.current.scale);
        camera.near=Math.max(.000001,Math.min(.01,distance/1000));camera.far=Math.max(100,distance+extent*20);controls.maxDistance=extent*20;
        camera.updateProjectionMatrix();controls.update();render();
      };
      const motion=createCutawayCameraMotion({read:readPose,apply:applyPose,reducedMotion:()=>motionPreference.matches,
        request:callback=>requestAnimationFrame(callback),cancel:id=>cancelAnimationFrame(id),now:()=>performance.now()});
      const interrupt=()=>{interacted=true;motion.cancel();};
      const stopKeyboardInterruption=bindCameraKeyboardInterruption(renderer.domElement,interrupt);
      const cancelDamping=()=>{if(dampingFrame!==null)cancelAnimationFrame(dampingFrame);dampingFrame=null;controls.enableDamping=false;controls.update();controls.enableDamping=!motionPreference.matches;};
      const orient=(action:CameraAction,immediate=false)=>{
        motion.cancel();cancelDamping();const pose=readPose();let next:CameraPose;
        if(action==="left"||action==="right")next=rotateCutawayCamera(pose,action==="left"?-.3:.3,fit);
        else if(action==="in"||action==="out"){
          const delta=camera.position.clone().sub(controls.target),length=Math.max(controls.minDistance,Math.min(controls.maxDistance,delta.length()*(action==="in"?.8:1.25)));
          next={...pose,position:delta.setLength(length).add(controls.target).toArray()};
        }else{
          const direction:readonly [number,number,number]=action==="top"?[0,1,.001]:action==="side"?[.2,0,1]:[.55,.6,1];
          const target:[number,number,number]=[0,-deepest*k*values.current.scale/2,0],{distance,offsetX,offsetY}=fit(direction);
          next={target,position:new T.Vector3(...direction).normalize().multiplyScalar(distance).add(new T.Vector3(...target)).toArray(),offset:[offsetX,offsetY]};
        }
        motion.move(next,immediate?0:action==="in"||action==="out"?180:320);
      };
      let lastScale=values.current.scale;
      const update=(v:Settings)=>{
        controls.mouseButtons.LEFT=v.navigation==="pan"?T.MOUSE.PAN:T.MOUSE.ROTATE;
        controls.touches.ONE=v.navigation==="pan"?T.TOUCH.PAN:T.TOUCH.ROTATE;
        volumeGroup.scale.y=v.scale;logGroup.scale.y=v.scale;frameGroup.scale.y=v.scale;logGroup.visible=v.logs;
        tickSprites.forEach(({sprite,fraction})=>sprite.position.set(-3.42,-frameDepth*fraction*v.scale,south));
        planePaint.opacity=v.surface*(surfaceTexture?1:.15);waters.forEach(m=>{m.opacity=v.water;});
        if(surfaceTexture){surfaceTexture.magFilter=v.smooth?T.LinearFilter:T.NearestFilter;surfaceTexture.minFilter=v.smooth?T.LinearFilter:T.NearestFilter;surfaceTexture.needsUpdate=true;}
        if(lastScale!==v.scale){
          motion.cancel();cancelDamping();const pose=readPose(),delta=-deepest*k*(v.scale-lastScale)/2;
          pose.position[1]+=delta;pose.target[1]+=delta;lastScale=v.scale;applyPose(pose);
        }else render();
      };
      const setSurface=(image:HTMLCanvasElement|null)=>{
        surfaceTexture?.dispose();surfaceTexture=image?new T.CanvasTexture(image):null;
        if(surfaceTexture)surfaceTexture.colorSpace=T.SRGBColorSpace;
        planePaint.map=surfaceTexture;planePaint.color.set(image?"#ffffff":"#83a4a7");planePaint.needsUpdate=true;
        update(values.current);
      };
      api.current={camera:action=>{interacted=true;orient(action);},update,setSurface,highlightRecord:(id)=>{highlightedRecord=id;render();}};setSurface(snapshotRef.current?.volume===volume?snapshotRef.current.image:null);
      let firstSize=true;
      const resize=()=>{if(!host.current)return;motion.cancel();const pose=readPose(),w=Math.max(1,host.current.clientWidth),h=Math.max(1,host.current.clientHeight);renderer.setSize(w,h);camera.aspect=w/h;camera.updateProjectionMatrix();
        if(firstSize){firstSize=false;if(previousCamera&&!fitFirstEvidence)applyPose(previousCamera.pose);else orient("reset",true);}else applyPose(pose);
      };
      const ray=new T.Raycaster(),point=new T.Vector2();let down=[0,0];
      const pointerDown=(e:PointerEvent)=>{interrupt();down=[e.clientX,e.clientY];};
      const pointerUp=(e:PointerEvent)=>{if(Math.hypot(e.clientX-down[0],e.clientY-down[1])>5)return;const b=renderer.domElement.getBoundingClientRect();point.set((e.clientX-b.left)/b.width*2-1,-(e.clientY-b.top)/b.height*2+1);ray.setFromCamera(point,camera);
        const hit=pickCutawaySource(ray,pickable.filter(m=>m.userData.record?values.current.logs:values.current.water>0));if(!hit)return;
        if(hit.object.userData.record){const r=hit.object.userData.record as Borehole,i=hit.object.userData.interval as DepthInterval|undefined;setSelection(null);setPickedLog({recordId:r.id,label:`${r.name}${i?` · ${i.top}–${i.bottom} ${r.depthUnit}: ${i.description}`:""}`});inspectRef.current(r,i);}else{setPickedLog(null);setSelection(hit.object.userData.envelope.id);}
      };
      const lost=(e:Event)=>{e.preventDefault();motion.cancel();setFailure("3D interrupted. The 2D locator and source ranges remain available below.");};
      renderer.domElement.addEventListener("pointerdown",pointerDown);renderer.domElement.addEventListener("pointerup",pointerUp);renderer.domElement.addEventListener("webglcontextlost",lost);controls.addEventListener("start",interrupt);
      const changed=()=>{render();if(controls.enableDamping&&dampingFrame===null&&!document.hidden)dampingFrame=requestAnimationFrame(()=>{dampingFrame=null;if(!disposed)controls.update();});};
      const preferenceChanged=()=>{motion.cancel();cancelDamping();};
      const visibilityChanged=()=>{if(document.hidden){motion.cancel();cancelDamping();}else render();};
      controls.addEventListener("change",changed);motionPreference.addEventListener("change",preferenceChanged);document.addEventListener("visibilitychange",visibilityChanged);
      const observer=new ResizeObserver(resize);observer.observe(host.current);resize();const disposeResources=cleanup;
      cleanup=()=>{cameraMemory.current={area,pose:readPose(),awaitingRecords,awaitingAquifer,interacted};stopKeyboardInterruption();motion.dispose();if(dampingFrame!==null)cancelAnimationFrame(dampingFrame);observer.disconnect();controls.removeEventListener("start",interrupt);controls.removeEventListener("change",changed);motionPreference.removeEventListener("change",preferenceChanged);document.removeEventListener("visibilitychange",visibilityChanged);renderer.domElement.removeEventListener("pointerdown",pointerDown);renderer.domElement.removeEventListener("pointerup",pointerUp);renderer.domElement.removeEventListener("webglcontextlost",lost);disposeResources();};
    }).catch(()=>{cleanup?.();cleanup=undefined;if(!disposed)setFailure("Aquifer 3D is unavailable on this device. Read the source ranges below and continue on the 2D locator.");});
    return()=>{disposed=true;api.current=null;cleanup?.();};
  },[volume,records,recordsLoading,aquiferLoading,retry,active,sceneRenderable]);
  useEffect(()=>{api.current?.setSurface(snapshot?.image??null);},[snapshot?.image]);
  useEffect(()=>{api.current?.update(values.current);},[surface,water,scale,logs,smooth,navigation]);
  useEffect(()=>{api.current?.highlightRecord(pickedLog?.recordId??null);},[pickedLog]);
  const selected=snapshot?.volume.envelopes.find(e=>e.id===selection);
  const showArea=()=>{
    focusAfterApply.current=true;
    // The global 2D callback animates even an already-flat map. Avoid that needless
    // transition; tilted/globe requests are retained by the session until settled.
    try{if(map&&(Math.abs(map.getPitch())>.1||Math.abs(map.getBearing())>.1||map.getProjection()?.type!=="mercator"))onFlatMap();}catch{ /* The session waits for style readiness and explains the hold. */ }
    areaSession.current?.prepare();
  };
  const zoomLocal=()=>{
    if(!map)return;
    try{
      const b=locatorBounds(map),span=Math.max(b[2]-b[0],b[3]-b[1]),c=map.getCenter();
      if(c.lng < -102.1 || c.lng > -94.5 || c.lat < 36.9 || c.lat > 40.1){setStatus("Move the map into Kansas, or open the High Plains example.");return;}
      const zoom=map.getZoom()+Math.max(0,Math.log2(span/.35));
      map.jumpTo({zoom,pitch:0,bearing:0});showArea();
    }catch{setStatus("The map is not ready yet. Retry when the map appears.");}
  };
  const zoomSelectedArea=(direction:"in"|"out")=>{
    if(!map)return;
    try{
      const duration=matchMedia("(prefers-reduced-motion: reduce)").matches?0:220;
      if(direction==="in")map.zoomIn({duration});else map.zoomOut({duration});
      // The manual session waits for moveend and captures the new map extent.
      // A normal drag remains only a preview until the user chooses Show.
      areaSession.current?.prepare();
    }catch{setStatus("The selector map is not ready to zoom. Retry when it appears.");}
  };
  const example=()=>{if(!map)return;map.jumpTo({center:[-100.5,38.5],zoom:11,pitch:0,bearing:0});showArea();};
  const frameReady=frame&&validVolumeBounds(frame),hasScene=Boolean(snapshot);
  return <section className={`${s.cutawayExplorer} ${s.areaExplorer}`} data-ready={hasScene} aria-label="4D area underlay from source records">
    <div className={s.cutawayWorkspace}>
      <aside className={s.cutawayLocator} aria-label="Choose the underlay area">
        <div className={s.cutawayLocatorTitle}><strong>{hasScene?"Selected area":"Choose an area"}</strong><span>2D MAP</span></div>
        <div ref={onLocatorSlot} className={s.cutawayLocatorMap} aria-label="Linked 2D selector map position" />
        <div className={s.cutawayLocatorActions}><button type="button" disabled={!map} onClick={frame&&!frameReady?zoomLocal:showArea}>{frame&&!frameReady?"Zoom in & explore":hasScene&&previewChanged?"Show new area":"Show this area"} <span aria-hidden="true">↗</span></button><button type="button" aria-label="Zoom selector map and selected area in" title="Zoom the map and update the selected cutaway" onClick={()=>zoomSelectedArea("in")}>+</button><button type="button" aria-label="Zoom selector map and selected area out" title="Zoom the map and update the selected cutaway" onClick={()=>zoomSelectedArea("out")}>−</button></div>
        <p className={s.areaFrameState}>{previewChanged&&snapshot?"Map preview changed. The cutaway still shows your selected area.":frame&&!frameReady?"This view is too broad for a local cutaway. Zoom in & explore keeps the map center and frames a smaller area.":hasScene?"Use the map +/− to zoom and update the selected area; pan, then Show for a new location.":"Pan to a place in Kansas, then show its recorded columns."}</p>
        <div className={s.areaProgress} role="status"><p>{status}</p>{snapshot&&<p>{recordsLoading?"Loading well and core records…":`${drawn?.recordCount??0} plotted columns · ${records.length} records at this time${partial?" · partial coverage":""}`}</p>}</div>
        <button type="button" className={s.areaExample} onClick={example}>Try High Plains example</button>
        <details className={s.areaLocationTools}><summary>Map movement</summary><div className={s.actions}>{[["←",-70,0],["↑",0,-70],["↓",0,70],["→",70,0]].map(([label,x,y])=><button type="button" key={String(label)} aria-label={`Pan selector ${label}`} onClick={()=>map?.panBy([Number(x),Number(y)],{duration:0})}>{label}</button>)}</div><button type="button" onClick={onFlatMap}>Reset to 2D</button></details>
        {snapshot&&<details className={s.areaCoverage}><summary>Coverage &amp; sources</summary><p>{recordStatus}</p><p>{surfaceStatus}</p><p>Selected frame: {snapshot.volume.bounds.map(n=>n.toFixed(4)).join(", ")}. Up to 50 records / 400 intervals. {drawn?.clipped?"Some depths or intervals reach the display limit.":""}</p><p>Each record retains its own depth reference. The surface is flat map context; widths are illustrative.</p></details>}
      </aside>
      <section ref={modelFocus} tabIndex={-1} className={s.areaModel} aria-label="Selected-area 3D cutaway">
        {!hasScene?<div className={s.areaStart}><span className={s.cutawayEyebrow}>UNDERGROUND</span><h3>A place, then a cutaway.</h3><p>Choose the area on the map. Its recorded logs will appear below the surface, ready to orbit and explore through record time.</p><p>Unknown ground stays empty. Aquifer ranges are an optional 2022–2024 source layer.</p></div>:<>
        <div className={s.areaModelHeading}><h3>3D cutaway</h3><span>Independent records · unknown ground stays empty</span></div>
        {sceneRenderable&&<div className={s.cutawayStage}>
          <div ref={host} className={s.cutawayCanvas} hidden={!!failure} />
          {failure&&<div className={s.cutawayEmpty}><h4>3D view unavailable</h4><p role="alert">{failure}</p><button type="button" onClick={()=>{setFailure("");setRetry(v=>v+1);}}>Retry 3D view</button></div>}
          {!failure&&<div className={s.cutawayCamera} aria-label="Area 3D navigation"><button type="button" aria-pressed={navigation==="orbit"} onClick={()=>setNavigation("orbit")}>Orbit</button><button type="button" aria-pressed={navigation==="pan"} onClick={()=>setNavigation("pan")}>Move</button><button type="button" onClick={()=>api.current?.camera("top")}>Surface image</button><button type="button" aria-pressed={smooth} onClick={()=>setSmooth(v=>!v)}>{smooth?"Smooth image":"Exact pixels"}</button>{([['reset','Reset view'],['in','+'],['out','−']] as const).map(([action,label])=><button type="button" key={action} aria-label={action==='in'?'Zoom in':action==='out'?'Zoom out':label} onClick={()=>api.current?.camera(action)}>{label}</button>)}</div>}
          <div className={s.cutawaySceneLabel}><span>{navigation==="pan"?"Drag to move":"Drag to orbit"} · scroll to zoom · select a source</span></div>
          <div className={s.cutawayStamp}>{scale}× DEPTH <span>·</span> {snapshot?.image?"SELECTED-AREA MAP":"FLAT REFERENCE PLANE · MAP IMAGE UNAVAILABLE"}</div>
        </div>}
        {!recordsLoading&&!drawn?.recordCount&&<div className={s.areaEmptyRecords} role="status"><strong>No recorded intervals at this time.</strong><p>{recordStatus}</p><button type="button" onClick={onResetRecords}>Reset record filters</button><button type="button" onClick={example}>Try High Plains example</button></div>}
        {recordsAvailable>0?recordNavigation:recordsLoading?<p className={s.areaLoading} role="status">Loading dated records for time navigation…</p>:null}
        </>}
      </section>
    </div>
    {hasScene&&<><div className={s.cutawayReadout} aria-live="polite"><span className={s.cutawayEyebrow}>INSPECT</span>{pickedLog?<span>{pickedLog.label}</span>:selected?<span>Water-table depth {selected.depthFeet.join("–")} ft · thickness {selected.thicknessFeet.join("–")} ft · outer range {selected.shallowMeters.toFixed(1)}–{selected.deepMeters.toFixed(1)} m.</span>:<span>Select a column or blue range to read its source.</span>}</div>
    <div className={s.areaTools}>
      <details className={s.areaAppearance}><summary>View settings</summary><div className={s.areaAppearanceGrid}>
        <label className={s.cutawayRange}>Surface map <output>{Math.round(surface*100)}%</output><input aria-label="Surface map opacity" type="range" min="0" max="100" value={surface*100} onChange={e=>setSurface(Number(e.target.value)/100)} /></label>
        <p className={s.muted}>Smooth image changes only how the captured basemap pixels are drawn. Recorded well and aquifer values are unchanged.</p>
        <label className={s.cutawayRange}>Aquifer range <output>{Math.round(water*100)}%</output><input aria-label="Aquifer opacity" type="range" min="0" max="100" value={water*100} onChange={e=>setWater(Number(e.target.value)/100)} /></label>
        <label className={s.cutawayScale}>Vertical scale <select aria-label="Cutaway vertical scale" value={scale} onChange={e=>setScale(Number(e.target.value))}>{[1,10,25,50,100,250,500].map(n=><option key={n} value={n}>{n}×</option>)}</select></label>
        <button type="button" aria-pressed={logs} onClick={()=>setLogs(v=>!v)}>Show recorded columns</button>
        <div className={s.actions} aria-label="Area camera presets">{([['top','Top'],['side','Side'],['left','Rotate left'],['right','Rotate right']] as const).map(([action,label])=><button type="button" key={action} disabled={!!failure} onClick={()=>api.current?.camera(action)}>{label}</button>)}</div>
      </div></details>
      <details className={s.cutawayEvidence}><summary>Aquifer legend &amp; evidence <span>{snapshot?.aquiferState==="unavailable"?"unavailable":snapshot?.aquiferState==="loading"?"loading":`${snapshot?.volume.envelopes.length??0} ranges`}</span></summary>
        <div className={s.cutawayLegend}><span><i data-kind="log"/>Log descriptions · illustrative width</span><span><i data-kind="core"/>Core inventory envelopes</span><span><i data-kind="aquifer"/>Aquifer uncertainty · 2022–2024</span><span><i data-kind="unknown"/>Unobserved / unlogged</span></div>
        <p>Blue marks possible outer depth ranges, not a filled reservoir or past groundwater. No continuous geology or caves are inferred.</p><p>{status}</p>
        {snapshot&&<><p>Depth clipping at {drawn?.limit.toFixed(1)} m. Source polygon generalization: 0.0005°. Missing/open-ended classes are withheld.</p><div className={s.cutawaySourceList}>{snapshot.volume.envelopes.map(e=><button type="button" key={e.id} aria-pressed={selection===e.id} onClick={()=>{setPickedLog(null);setSelection(e.id);}}>Depth {e.depthFeet.join("–")} ft · thickness {e.thicknessFeet.join("–")} ft</button>)}</div></>}
        <a href={KGS_ATLAS_URL} target="_blank" rel="noreferrer">Read the KGS Atlas ↗</a>
      </details>{sliceEntry}
    </div></>}
  </section>;
}
