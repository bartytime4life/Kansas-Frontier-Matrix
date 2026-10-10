"use client";
import { useEffect, useMemo, useRef, useState, type ReactNode } from "react";
import type { Map as MapLibreMap } from "./maplibre-seam";
import { startAquiferVolumeWorker } from "./subsurface-workers";
import { projectVolumePosition, volumeDepthScale, validVolumeBounds } from "./aquifer-volume";
import { materialFor, materialInfo } from "./subsurface-materials";
import { type Borehole, type DepthInterval } from "./subsurface-model";
import { cutawayCameraFit, cutawayRecords, pickCutawaySource } from "./cutaway-model";
import { bindCameraKeyboardInterruption, createCutawayCameraMotion, createCutawayRenderSchedule, rotateCutawayCamera, type CameraPose } from "./cutaway-camera";
import { KGS_ATLAS_URL } from "./aquifer-layers";
import s from "./subsurface.module.css";
import { aquiferGeometries } from "./aquifer-volume-mesh";
import { startAquiferView, locatorBounds, type AquiferViewSnapshot } from "./aquifer-view-session";
import SelectedSurfaceMap from "./selected-surface-map";
import type { SurfaceCapture } from "./selected-surface";
import { startCutawaySurfaceDetail, detailBoundsFromSurface, type SurfaceDetailFrame } from "./cutaway-surface-detail";
type VolumeBounds = [number,number,number,number];
type Snapshot = AquiferViewSnapshot<HTMLCanvasElement>;
type CameraAction="reset"|"top"|"side"|"left"|"right"|"in"|"out";
type Settings={surface:number;water:number;scale:number;logs:boolean;smooth:boolean;navigation:"orbit"|"pan"};
export default function AquiferVolumeView({basemap,onBasemap,onLayers,active=true,map,records,onFlatMap,onInspect,onLocatorSlot,sliceEntry,resourcePanel,onArea,recordsLoading,recordStatus,partial,recordNavigation,recordsAvailable,onResetRecords}:{basemap?:string;onBasemap?:(key:"standard"|"imagery"|"kansas-aerial"|"topo")=>void;onLayers?:()=>void;active?:boolean;map:MapLibreMap|null;records:Borehole[];onFlatMap:()=>void;onLocate:(point:[number,number],retainView?:boolean)=>void;onInspect:(record:Borehole,interval?:DepthInterval)=>void;locator:{anchor:[number,number];pinned:boolean};onLocatorSlot:(slot:HTMLDivElement|null)=>void;sliceEntry?:ReactNode;resourcePanel?:ReactNode;onArea:(bounds:VolumeBounds|null)=>void;recordsLoading:boolean;recordStatus:string;partial:boolean;recordNavigation:ReactNode;recordsAvailable:number;onResetRecords:()=>void}){
  const [snapshot,setSnapshot]=useState<Snapshot|null>(null),[status,setStatus]=useState("Preparing the current locator area…"),[retry,setRetry]=useState(0);
  const [surfaceStatus,setSurfaceStatus]=useState(""),[previewChanged,setPreviewChanged]=useState(false);
  const [surfaceMode,setSurfaceMode]=useState(false);
  const [detailCapture,setDetailCapture]=useState<SurfaceCapture|null>(null),[detailStatus,setDetailStatus]=useState("Preparing high-detail surface…"),[detailShown,setDetailShown]=useState(false);
  const [detailPixels,setDetailPixels]=useState(4096),[detailRetry,setDetailRetry]=useState(0);
  const detailRenderer=useRef<ReturnType<typeof startCutawaySurfaceDetail>|null>(null),detailFrame=useRef<SurfaceDetailFrame|null>(null);
  const [frame,setFrame]=useState<VolumeBounds|null>(null);
  const modelFocus=useRef<HTMLElement|null>(null),focusAfterApply=useRef(false);
  const [navigation,setNavigation]=useState<"orbit"|"pan">("orbit");
  const areaSession=useRef<{prepare:()=>void}|null>(null),onAreaRef=useRef(onArea);
  useEffect(()=>{onAreaRef.current=onArea;},[onArea]);
  const [surface,setSurface]=useState(1),[water,setWater]=useState(.22),[scale,setScale]=useState(25),[logs,setLogs]=useState(true),[smooth,setSmooth]=useState(false);
  const [failure,setFailure]=useState(""),[selection,setSelection]=useState<string|null>(null);
  const [pickedLog,setPickedLog]=useState<{label:string;recordId:string}|null>(null);
  const host=useRef<HTMLDivElement>(null),api=useRef<{camera:(action:CameraAction)=>void;update:(v:Settings)=>void;setSurface:(image:HTMLCanvasElement|null)=>void;setDetail:(frame:SurfaceDetailFrame|null)=>boolean;highlightRecord:(id:string|null)=>void;focusRecord:(id:string)=>void}|null>(null);
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
  const sampleRecords=useMemo(()=>Array.from(new Map(drawn?.intervals.map(({record})=>[record.id,record])).values()),[drawn]);
  const pickedRecord=sampleRecords.find(record=>record.id===pickedLog?.recordId);
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
    if(!active||surfaceMode||!detailCapture||detailCapture.bounds.join(",")!==volume?.bounds.join(","))return;
    api.current?.setSurface(null);
    setDetailShown(false);
    const controller=startCutawaySurfaceDetail({capture:detailCapture,pixels:detailPixels,onFrame:frame=>{detailFrame.current=frame;setDetailShown(api.current?.setDetail(frame)??false);},onStatus:setDetailStatus});
    detailRenderer.current=controller;
    return()=>{controller.dispose();detailRenderer.current=null;detailFrame.current=null;api.current?.setDetail(null);setDetailShown(false);};
  },[active,surfaceMode,detailCapture,detailPixels,detailRetry,volume?.bounds]);
  useEffect(()=>{
    if(!active||surfaceMode||!sceneRenderable||!volume||!host.current)return;
    setFailure("");
    let disposed=false,cleanup:(()=>void)|undefined;
    void Promise.all([import("three"),import("three/addons/controls/OrbitControls.js")]).then(([T,{OrbitControls}])=>{
      if(disposed||!host.current)return;
      const renderer=new T.WebGLRenderer({antialias:true});renderer.setPixelRatio(Math.min(devicePixelRatio,2));
      const resources:{dispose:()=>void}[]=[];cleanup=()=>{resources.forEach(r=>r.dispose());renderer.dispose();renderer.forceContextLoss();renderer.domElement.remove();};
      renderer.domElement.tabIndex=0;renderer.domElement.setAttribute("aria-label","3D cutaway of independent well logs and aquifer source ranges below a flat locator map. Drag to orbit or choose Move to pan; arrows pan, modified arrows rotate, and buttons provide alternatives. Zoom stays centered on your inspection target; Reset view recovers the full slice.");host.current.append(renderer.domElement);
      const scene=new T.Scene();scene.background=new T.Color("#101b20");const camera=new T.PerspectiveCamera(40,1,.01,500);
      const controls=new OrbitControls(camera,renderer.domElement),motionPreference=matchMedia("(prefers-reduced-motion: reduce)");
      controls.enableDamping=!motionPreference.matches;controls.dampingFactor=.14;controls.maxPolarAngle=Math.PI*.92;controls.zoomToCursor=false;controls.listenToKeyEvents(renderer.domElement);resources.push(controls);
      const bounds=volume.bounds,k=volumeDepthScale(bounds),area=bounds.join(",");
      controls.minDistance=Math.max(.00001,2*k); // Two metres in this slice, independent of its width.
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
      const plane=new T.Mesh(planeGeometry,planePaint);plane.position.y=0;plane.renderOrder=3;scene.add(plane);
      const borderGeom=new T.EdgesGeometry(planeGeometry),borderPaint=new T.LineBasicMaterial({color:"#d2ad75"});resources.push(borderGeom,borderPaint);const border=new T.LineSegments(borderGeom,borderPaint);border.position.y=.001;scene.add(border);
      let detailMesh:InstanceType<typeof T.Mesh>|null=null,detailTexture:InstanceType<typeof T.CanvasTexture>|null=null;
      const clearDetail=()=>{if(detailMesh){scene.remove(detailMesh);detailMesh.geometry.dispose();(detailMesh.material as InstanceType<typeof T.Material>).dispose();detailMesh=null;}detailTexture?.dispose();detailTexture=null;};
      resources.push({dispose:clearDetail});
      const surfaceRay=new T.Raycaster(),surfacePlane=new T.Plane(new T.Vector3(0,1,0),0),surfaceHit=new T.Vector3();
      const volumeGroup=new T.Group(),logGroup=new T.Group(),surfaceMarkers=new T.Group();scene.add(volumeGroup,logGroup,surfaceMarkers);
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
      const anchors:InstanceType<typeof T.Mesh>[]=[];
      const diagramColumns:{mesh:InstanceType<typeof T.Mesh>;edge:InstanceType<typeof T.LineSegments>;edgePaint:InstanceType<typeof T.LineBasicMaterial>;recordId:string}[]=[];
      let highlightedRecord:string|null=pickedLogRef.current?.recordId??null;
      for(const {record,interval,top,bottom} of plotted.intervals){
        const p=projectVolumePosition(...record.coordinates,bounds);
        const geometry=new T.CylinderGeometry(.5,.5,(bottom-top)*k,12),paint=new T.MeshBasicMaterial({color:materialInfo(materialFor(interval,record.kind)).color});resources.push(geometry,paint);
        const mesh=new T.Mesh(geometry,paint);mesh.position.set(p.x,-(top+bottom)/2*k,p.z);mesh.userData.record=record;mesh.userData.interval=interval;mesh.renderOrder=4;logGroup.add(mesh);pickable.push(mesh);
        const edgeGeometry=new T.EdgesGeometry(geometry,50),edgePaint=new T.LineBasicMaterial({color:"#c9c3af",transparent:true,opacity:.65});resources.push(edgeGeometry,edgePaint);
        const edge=new T.LineSegments(edgeGeometry,edgePaint);edge.renderOrder=5;mesh.add(edge);diagramColumns.push({mesh,edge,edgePaint,recordId:record.id});
        if(!collars.has(record.id)){
          // Recorded coordinates stay on the flat ground, outside exaggerated depth groups.
          collars.add(record.id);const collarGeometry=new T.RingGeometry(.34,.5,32);collarGeometry.rotateX(-Math.PI/2);
          const dotGeometry=new T.CircleGeometry(.09,16);dotGeometry.rotateX(-Math.PI/2);
          const collarPaint=new T.MeshBasicMaterial({color:record.kind==="core"?"#baa2df":"#e0b46f",side:T.DoubleSide,depthWrite:false,polygonOffset:true,polygonOffsetFactor:-2,polygonOffsetUnits:-2});resources.push(collarGeometry,dotGeometry,collarPaint);
          const collar=new T.Mesh(collarGeometry,collarPaint);collar.position.set(p.x,0,p.z);collar.userData.record=record;collar.userData.surfaceAnchor=true;collar.renderOrder=6;surfaceMarkers.add(collar);
          const dot=new T.Mesh(dotGeometry,collarPaint);dot.userData.record=record;dot.renderOrder=6;collar.add(dot);anchors.push(collar);pickable.push(collar,dot);
        }
      }
      scene.add(new T.HemisphereLight(0xd2eeff,0x194955,2.5));const light=new T.DirectionalLight(0xffffff,2);light.position.set(4,6,3);scene.add(light);
      const worldPosition=new T.Vector3(),cameraSpace=new T.Vector3();
      const worldPerPixel=(object:InstanceType<typeof T.Object3D>)=>{
        object.getWorldPosition(worldPosition);cameraSpace.copy(worldPosition).applyMatrix4(camera.matrixWorldInverse);
        return 2*Math.max(camera.near,Math.abs(cameraSpace.z))*Math.tan(T.MathUtils.degToRad(camera.fov)/2)/Math.max(1,renderer.domElement.clientHeight);
      };
      const draw=()=>{
        if(disposed||document.hidden)return;
        // Wheel/trackpad navigation must update clipping too, not only camera buttons.
        const extent=Math.max(6,south-north,deepest*k*values.current.scale);
        camera.near=Math.max(.000001,Math.min(.01,camera.position.distanceTo(controls.target)/1000));
        camera.far=Math.max(100,camera.position.length()+extent*4);
        camera.updateProjectionMatrix();scene.updateMatrixWorld(true);camera.updateMatrixWorld(true);
        // Screen-legible diagram widths, never a claim about physical well diameter.
        for(const {mesh,edgePaint,recordId} of diagramColumns){
          const chosen=recordId===highlightedRecord,diameter=worldPerPixel(mesh)*(chosen?11:9);
          mesh.scale.x=diameter;mesh.scale.z=diameter;
          edgePaint.color.set(chosen?"#ffe2a3":"#c9c3af");edgePaint.opacity=chosen?1:.65;
        }
        for(const anchor of anchors){
          const diameter=worldPerPixel(anchor)*(anchor.userData.record.id===highlightedRecord?18:14);
          anchor.scale.set(diameter,1,diameter);
        }
        const tickTop=tickSprites[0]?.sprite.position.clone().project(camera),tickBottom=tickSprites.at(-1)?.sprite.position.clone().project(camera);
        const tickPixels=tickTop&&tickBottom?Math.abs(tickTop.y-tickBottom.y)*renderer.domElement.clientHeight/2:0;
        for(const {sprite,fraction} of tickSprites){
          const pixel=worldPerPixel(sprite);sprite.scale.set(pixel*90,pixel*24,1);
          sprite.visible=fraction===1||(fraction===0&&tickPixels>=30)||(fraction===.5&&tickPixels>=66)||(fraction!==0&&fraction!==.5&&tickPixels>=120);
        }
        renderer.render(scene,camera);
        const visible:{x:number;z:number}[]=[];
        for(const x of [-1,0,1])for(const y of [-1,0,1]){surfaceRay.setFromCamera(new T.Vector2(x,y),camera);if(surfaceRay.ray.intersectPlane(surfacePlane,surfaceHit))visible.push({x:surfaceHit.x,z:surfaceHit.z});}
        // Include any surface corner still on screen, including views grazing the horizon.
        for(const x of [-3,3])for(const z of [north,south]){const p=new T.Vector3(x,0,z).project(camera);if(Math.abs(p.x)<=1&&Math.abs(p.y)<=1&&p.z>=-1&&p.z<=1)visible.push({x,z});}
        const visibleBounds=detailBoundsFromSurface(bounds,visible);if(visibleBounds)detailRenderer.current?.update(visibleBounds);
      };
      let contextLost=false;
      const renderSchedule=createCutawayRenderSchedule({draw,updateControls:()=>controls.update(),damping:()=>controls.enableDamping,
        active:()=>!disposed&&!document.hidden&&!contextLost,request:callback=>requestAnimationFrame(callback),cancel:id=>cancelAnimationFrame(id)});
      resources.push({dispose:()=>renderSchedule.dispose()});
      const render=renderSchedule.invalidate;
      const fit=(direction:readonly [number,number,number])=>cutawayCameraFit(6,south-north,deepest*k*values.current.scale,camera.aspect,direction,renderer.domElement.clientHeight);
      let viewOffset:[number,number]=[0,0];
      const readPose=():CameraPose=>({position:camera.position.toArray(),target:controls.target.toArray(),offset:[...viewOffset]});
      const applyPose=(pose:CameraPose)=>{
        camera.position.fromArray(pose.position);controls.target.fromArray(pose.target);viewOffset=[...pose.offset];
        const w=Math.max(1,renderer.domElement.clientWidth),h=Math.max(1,renderer.domElement.clientHeight);
        camera.setViewOffset(w,h,viewOffset[0]*w/2,-viewOffset[1]*h/2,w,h);
        // A useful overview limit keeps the slice visible and zoom reversals bounded.
        controls.maxDistance=fit([.55,.6,1]).distance*4;
        camera.updateProjectionMatrix();controls.update();render();
      };
      const motion=createCutawayCameraMotion({read:readPose,apply:applyPose,reducedMotion:()=>motionPreference.matches,
        request:callback=>requestAnimationFrame(callback),cancel:id=>cancelAnimationFrame(id),now:()=>performance.now()});
      const interrupt=()=>{interacted=true;motion.cancel();};
      const stopKeyboardInterruption=bindCameraKeyboardInterruption(renderer.domElement,interrupt);
      const cancelDamping=()=>{renderSchedule.cancel();controls.enableDamping=false;controls.update();controls.enableDamping=!motionPreference.matches;};
      const orient=(action:CameraAction,immediate=false)=>{
        motion.cancel();cancelDamping();const pose=readPose();let next:CameraPose;
        if(action==="left"||action==="right")next=rotateCutawayCamera(pose,action==="left"?-.3:.3,fit);
        else if(action==="in"||action==="out"){
          const delta=camera.position.clone().sub(controls.target),length=Math.max(controls.minDistance,Math.min(controls.maxDistance,delta.length()*(action==="in"?.8:1.25)));
          next={...pose,position:delta.setLength(length).add(controls.target).toArray()};
        }else{
          const direction:readonly [number,number,number]=action==="top"?[0,1,.001]:action==="side"?[.2,0,1]:[.55,.6,1];
          const target:[number,number,number]=[0,action==="top"?0:-deepest*k*values.current.scale/2,0],{distance,offsetX,offsetY}=action==="top"?cutawayCameraFit(6,south-north,0,camera.aspect,direction,renderer.domElement.clientHeight):fit(direction);
          next={target,position:new T.Vector3(...direction).normalize().multiplyScalar(distance).add(new T.Vector3(...target)).toArray(),offset:[offsetX,offsetY]};
        }
        // Apply each zoom step immediately: repeated clicks must not cancel pending steps.
        motion.move(next,immediate||action==="in"||action==="out"?0:320);
      };
      let lastScale=values.current.scale;
      const sampleTexture=(texture:InstanceType<typeof T.CanvasTexture>|null,smooth:boolean)=>{
        if(!texture)return;
        const filter=smooth?T.LinearFilter:T.NearestFilter;
        // Appearance-only changes must not re-upload the unchanged map pixels.
        if(texture.magFilter===filter&&texture.minFilter===filter)return;
        texture.magFilter=filter;texture.minFilter=filter;texture.needsUpdate=true;
      };
      const update=(v:Settings)=>{
        controls.mouseButtons.LEFT=v.navigation==="pan"?T.MOUSE.PAN:T.MOUSE.ROTATE;
        controls.touches.ONE=v.navigation==="pan"?T.TOUCH.PAN:T.TOUCH.ROTATE;
        volumeGroup.scale.y=v.scale;logGroup.scale.y=v.scale;frameGroup.scale.y=v.scale;logGroup.visible=v.logs;surfaceMarkers.visible=v.logs;
        tickSprites.forEach(({sprite,fraction})=>sprite.position.set(-3.42,-frameDepth*fraction*v.scale,south));
        planePaint.opacity=v.surface*(surfaceTexture?1:.15);waters.forEach(m=>{m.opacity=v.water;});
        if(detailMesh)(detailMesh.material as InstanceType<typeof T.MeshBasicMaterial>).opacity=v.surface;
        sampleTexture(detailTexture,v.smooth);sampleTexture(surfaceTexture,v.smooth);
        if(lastScale!==v.scale){
          motion.cancel();cancelDamping();const pose=readPose(),delta=controls.target.y===0?0:-deepest*k*(v.scale-lastScale)/2;
          pose.position[1]+=delta;pose.target[1]+=delta;lastScale=v.scale;applyPose(pose);
        }else render();
      };
      const setSurface=(image:HTMLCanvasElement|null)=>{
        surfaceTexture?.dispose();surfaceTexture=image?new T.CanvasTexture(image):null;
        if(surfaceTexture)surfaceTexture.colorSpace=T.SRGBColorSpace;
        planePaint.map=surfaceTexture;planePaint.color.set(image?"#ffffff":"#83a4a7");planePaint.needsUpdate=true;
        update(values.current);
      };
      const setDetail=(frame:SurfaceDetailFrame|null)=>{
        clearDetail();plane.visible=true;if(!frame){render();return false;}
        const [w,southLat,e,northLat]=frame.bounds,clipped:[number,number,number,number]=[Math.max(w,bounds[0]),Math.max(southLat,bounds[1]),Math.min(e,bounds[2]),Math.min(northLat,bounds[3])];
        if(clipped[2]<=clipped[0]||clipped[3]<=clipped[1]){render();return false;}
        const nw=projectVolumePosition(clipped[0],clipped[3],bounds),se=projectVolumePosition(clipped[2],clipped[1],bounds),wholeNW=projectVolumePosition(w,northLat,bounds),wholeSE=projectVolumePosition(e,southLat,bounds);
        detailTexture=new T.CanvasTexture(frame.image);detailTexture.colorSpace=T.SRGBColorSpace;detailTexture.generateMipmaps=false;sampleTexture(detailTexture,values.current.smooth);detailTexture.anisotropy=renderer.capabilities?.getMaxAnisotropy?.()??1;
        detailTexture.repeat.set((se.x-nw.x)/(wholeSE.x-wholeNW.x),(se.z-nw.z)/(wholeSE.z-wholeNW.z));detailTexture.offset.set((nw.x-wholeNW.x)/(wholeSE.x-wholeNW.x),(wholeSE.z-se.z)/(wholeSE.z-wholeNW.z));
        const geometry=new T.PlaneGeometry(se.x-nw.x,se.z-nw.z);geometry.rotateX(-Math.PI/2);
        const paint=new T.MeshBasicMaterial({map:detailTexture,transparent:true,opacity:values.current.surface,side:T.DoubleSide,depthWrite:false});
        detailMesh=new T.Mesh(geometry,paint);detailMesh.position.set((nw.x+se.x)/2,0,(nw.z+se.z)/2);detailMesh.renderOrder=3;scene.add(detailMesh);plane.visible=false;render();return true;
      };
      const focusRecord=(id:string)=>{
        const record=plotted.intervals.find(item=>item.record.id===id)?.record;if(!record)return;
        interrupt();cancelDamping();const p=projectVolumePosition(...record.coordinates,bounds),target:[number,number,number]=[p.x,0,p.z];
        const distance=Math.max(controls.minDistance,100*k/Math.tan(T.MathUtils.degToRad(camera.fov)/2));
        motion.move({target,position:new T.Vector3(0,1,.001).normalize().multiplyScalar(distance).add(new T.Vector3(...target)).toArray(),offset:[0,0]},motionPreference.matches?0:320);
      };
      api.current={camera:action=>{interacted=true;orient(action);},update,setSurface,setDetail,highlightRecord:(id)=>{highlightedRecord=id;render();},focusRecord};setSurface(snapshotRef.current?.volume===volume?snapshotRef.current.image:null);if(detailFrame.current)setDetailShown(setDetail(detailFrame.current));
      let firstSize=true;
      const resize=()=>{if(!host.current)return;motion.cancel();const pose=readPose(),w=Math.max(1,host.current.clientWidth),h=Math.max(1,host.current.clientHeight);renderer.setSize(w,h);camera.aspect=w/h;camera.updateProjectionMatrix();
        if(firstSize){firstSize=false;if(previousCamera&&!fitFirstEvidence)applyPose(previousCamera.pose);else orient("reset",true);}else applyPose(pose);
      };
      const ray=new T.Raycaster(),point=new T.Vector2();let down:{id:number;x:number;y:number}|null=null;
      const pointerDown=(e:PointerEvent)=>{interrupt();down=e.isPrimary && e.button===0?{id:e.pointerId,x:e.clientX,y:e.clientY}:null;};
      const pointerCancel=()=>{down=null;};
      const pointerUp=(e:PointerEvent)=>{const start=down;down=null;if(!start||start.id!==e.pointerId||e.button!==0||Math.hypot(e.clientX-start.x,e.clientY-start.y)>5)return;const b=renderer.domElement.getBoundingClientRect();point.set((e.clientX-b.left)/b.width*2-1,-(e.clientY-b.top)/b.height*2+1);ray.setFromCamera(point,camera);
        const hit=pickCutawaySource(ray,pickable.filter(m=>m.userData.record?values.current.logs:values.current.water>0),{camera,width:b.width,height:b.height,x:e.clientX-b.left,y:e.clientY-b.top,radius:e.pointerType==="touch"?16:10});if(!hit)return;
        if(hit.object.userData.record){const r=hit.object.userData.record as Borehole,i=hit.object.userData.interval as DepthInterval|undefined;setSelection(null);setPickedLog({recordId:r.id,label:`${r.name}${i?` · ${i.top}–${i.bottom} ${r.depthUnit}: ${i.description}`:""}`});inspectRef.current(r,i);}else{setPickedLog(null);setSelection(hit.object.userData.envelope.id);}
      };
      const lost=(e:Event)=>{e.preventDefault();contextLost=true;motion.cancel();renderSchedule.cancel();setFailure("3D interrupted. The 2D locator and source ranges remain available below.");};
      renderer.domElement.addEventListener("pointerdown",pointerDown);renderer.domElement.addEventListener("pointerup",pointerUp);renderer.domElement.addEventListener("pointercancel",pointerCancel);renderer.domElement.addEventListener("webglcontextlost",lost);controls.addEventListener("start",interrupt);
      const changed=renderSchedule.changed;
      const preferenceChanged=()=>{motion.cancel();cancelDamping();};
      const visibilityChanged=()=>{if(document.hidden){motion.cancel();cancelDamping();}else render();};
      controls.addEventListener("change",changed);motionPreference.addEventListener("change",preferenceChanged);document.addEventListener("visibilitychange",visibilityChanged);
      let resizeFrame:number|null=null;
      const observer=new ResizeObserver(()=>{if(resizeFrame!==null)cancelAnimationFrame(resizeFrame);resizeFrame=requestAnimationFrame(()=>{resizeFrame=null;if(!disposed)resize();});});observer.observe(host.current);resize();const disposeResources=cleanup;
      cleanup=()=>{cameraMemory.current={area,pose:readPose(),awaitingRecords,awaitingAquifer,interacted};stopKeyboardInterruption();motion.dispose();renderSchedule.dispose();observer.disconnect();if(resizeFrame!==null)cancelAnimationFrame(resizeFrame);controls.removeEventListener("start",interrupt);controls.removeEventListener("change",changed);motionPreference.removeEventListener("change",preferenceChanged);document.removeEventListener("visibilitychange",visibilityChanged);renderer.domElement.removeEventListener("pointerdown",pointerDown);renderer.domElement.removeEventListener("pointerup",pointerUp);renderer.domElement.removeEventListener("pointercancel",pointerCancel);renderer.domElement.removeEventListener("webglcontextlost",lost);disposeResources();};
    }).catch(()=>{cleanup?.();cleanup=undefined;if(!disposed)setFailure("Aquifer 3D is unavailable on this device. Read the source ranges below and continue on the 2D locator.");});
    return()=>{disposed=true;api.current=null;cleanup?.();};
  },[volume,records,recordsLoading,aquiferLoading,retry,active,sceneRenderable,surfaceMode]);
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
        {resourcePanel}
        <button type="button" className={s.areaExample} onClick={example}>Try High Plains example</button>
        <details className={s.areaLocationTools}><summary>Map movement</summary><div className={s.actions}>{[["←",-70,0],["↑",0,-70],["↓",0,70],["→",70,0]].map(([label,x,y])=><button type="button" key={String(label)} aria-label={`Pan selector ${label}`} onClick={()=>map?.panBy([Number(x),Number(y)],{duration:0})}>{label}</button>)}</div><button type="button" onClick={onFlatMap}>Reset to 2D</button></details>
        {snapshot&&<details className={s.areaCoverage}><summary>Coverage &amp; sources</summary><p>{recordStatus}</p><p>{surfaceStatus}</p><p>Selected frame: {snapshot.volume.bounds.map(n=>n.toFixed(4)).join(", ")}. Up to 50 records / 400 intervals. {drawn?.clipped?"Some depths or intervals reach the display limit.":""}</p><p>Each record retains its own depth reference. The surface is flat map context; widths are illustrative.</p></details>}
      </aside>
      <section ref={modelFocus} tabIndex={-1} className={s.areaModel} aria-label="Selected-area surface and cutaway">
        {!hasScene?<div className={s.areaStart}><span className={s.cutawayEyebrow}>UNDERGROUND</span><h3>A place, then a cutaway.</h3><p>Choose the area on the map. Its recorded logs will appear below the surface, ready to orbit and explore through record time.</p><p>Unknown ground stays empty. Aquifer ranges are an optional 2022–2024 source layer.</p></div>:<>
        <div className={s.areaModelHeading}><h3>{surfaceMode?"Surface map":"3D cutaway"}</h3><span>{surfaceMode?"Explore details within the selected slice":"Independent records · unknown ground stays empty"}</span></div>
        <div className={s.surfaceViewSwitch} aria-label="Selected-area view"><button type="button" aria-pressed={surfaceMode} onClick={()=>setSurfaceMode(true)}>Surface map</button><button type="button" aria-pressed={!surfaceMode} onClick={()=>setSurfaceMode(false)}>3D cutaway</button></div>
        <div className={s.surfaceDetailControls} aria-label="Basemap and surface detail">
          {onBasemap&&<label>Basemap <select aria-label="Cutaway basemap" value={basemap} onChange={event=>onBasemap(event.target.value as "standard"|"imagery"|"kansas-aerial"|"topo")}><option value="standard">Detailed streets &amp; buildings · vector</option><option value="kansas-aerial">Kansas aerial · 2024 · 1 foot</option><option value="imagery">Aerial &amp; satellite imagery · Esri</option><option value="topo">USGS topographic map</option>{!["standard","imagery","kansas-aerial","topo"].includes(basemap??"")&&<option value={basemap}>Current basemap</option>}</select></label>}
          {onLayers&&<button type="button" onClick={onLayers}>Choose map layers</button>}
          <label>3D surface detail <select aria-label="Cutaway surface resolution" value={detailPixels} onChange={event=>setDetailPixels(Number(event.target.value))}><option value={2048}>High · 2048 px</option><option value={4096}>Maximum · 4096 px</option></select></label>
          <button type="button" onClick={()=>setDetailRetry(v=>v+1)}>Refresh surface</button>
          <label className={s.cutawayRange}>Basemap opacity <output>{Math.round(surface*100)}%</output><input aria-label="Basemap opacity" type="range" min="0" max="100" value={surface*100} onChange={e=>setSurface(Number(e.target.value)/100)} /></label>
          <p>Opacity changes the map image and its display overlays. Recorded sample markers and source values stay unchanged.</p>
          <p>{detailCapture?.style.sources["kansas-ng911-2024"]?"Kansas NG911 aerial · February–April 2024 · approximately 1-foot source resolution. Exact local flight date unresolved; independent of map time.":"Provider basemap tiles. Imagery dates and resolution vary by location; refreshing is not a new acquisition."} Display context, not KFM evidence. <a href={detailCapture?.style.sources["kansas-ng911-2024"]?"https://storymaps.arcgis.com/stories/426fc98cba994ff99d0c9f21c96eef08":basemap==="imagery"?"https://www.arcgis.com/home/item.html?id=10df2279f9684e4a9f6a7f08febac2a9":basemap==="topo"?"https://basemap.nationalmap.gov/arcgis/rest/services/USGSTopo/MapServer":"https://openfreemap.org/"} target="_blank" rel="noreferrer">Provider &amp; imagery dates ↗</a> After changing layers, refresh the surface. If the selector has moved, show that area first.</p>
          {!surfaceMode&&<p role="status">{detailStatus} Crisp cells are the default; no detail is invented beyond the provider resolution.</p>}
        </div>
        {snapshot&&<SelectedSurfaceMap onCapture={setDetailCapture} refreshKey={`${basemap}:${detailRetry}`} source={map} bounds={snapshot.volume.bounds} image={snapshot.image} active={active&&surfaceMode} opacity={surface} smooth={smooth} onSmooth={()=>setSmooth(v=>!v)} />}
        <div hidden={surfaceMode}>
        {sampleRecords.length>0&&<div className={s.sampleLocationControls}>
          <label>Sample location <select aria-label="Sample location" value={pickedLog?.recordId??""} onChange={event=>{const record=sampleRecords.find(item=>item.id===event.target.value);if(record){setSelection(null);setPickedLog({recordId:record.id,label:record.name});inspectRef.current(record);}else setPickedLog(null);}}><option value="">Select a recorded well or core</option>{sampleRecords.map(record=><option key={record.id} value={record.id}>{record.kind==="core"?"Core":"Well"} · {record.name}</option>)}</select></label>
          <button type="button" disabled={!pickedRecord||!!failure} onClick={()=>{if(pickedRecord)api.current?.focusRecord(pickedRecord.id);}}>Zoom to sample</button>
          <p>{pickedRecord?`Recorded location: ${pickedRecord.coordinates[1].toFixed(6)}, ${pickedRecord.coordinates[0].toFixed(6)}. `:""}The dot marks the recorded location on the flat map; rings are selection aids. Location accuracy is not supplied here.</p>
        </div>}
        {sceneRenderable&&<div className={s.cutawayStage}>
          <div ref={host} className={s.cutawayCanvas} hidden={!!failure} />
          {failure&&<div className={s.cutawayEmpty}><h4>3D view unavailable</h4><p role="alert">{failure}</p><button type="button" onClick={()=>{setFailure("");setRetry(v=>v+1);}}>Retry 3D view</button></div>}
          {!failure&&<div className={s.cutawayCamera} aria-label="Area 3D navigation"><button type="button" aria-pressed={navigation==="orbit"} onClick={()=>setNavigation("orbit")}>Orbit</button><button type="button" aria-pressed={navigation==="pan"} onClick={()=>setNavigation("pan")}>Move</button><button type="button" onClick={()=>api.current?.camera("top")}>Top view</button><button type="button" aria-pressed={smooth} onClick={()=>setSmooth(v=>!v)}>{smooth?"Smooth image":"Exact pixels"}</button>{([['reset','Reset view'],['in','+'],['out','−']] as const).map(([action,label])=><button type="button" key={action} aria-label={action==='in'?'Zoom in':action==='out'?'Zoom out':label} onClick={()=>api.current?.camera(action)}>{label}</button>)}</div>}
          <div className={s.cutawaySceneLabel}><span>{navigation==="pan"?"Drag to move":"Drag to orbit"} · scroll to zoom · select a source</span></div>
          <div className={s.cutawayStamp}>{scale}× DEPTH <span>·</span> {detailShown?"HIGH-DETAIL MAP":snapshot?.image?"SELECTED-AREA MAP":"FLAT REFERENCE PLANE · MAP IMAGE UNAVAILABLE"}</div>
        </div>}
        {!recordsLoading&&!drawn?.recordCount&&<div className={s.areaEmptyRecords} role="status"><strong>No recorded intervals at this time.</strong><p>{recordStatus}</p><button type="button" onClick={onResetRecords}>Reset record filters</button><button type="button" onClick={example}>Try High Plains example</button></div>}
        {recordsAvailable>0?recordNavigation:recordsLoading?<p className={s.areaLoading} role="status">Loading dated records for time navigation…</p>:null}
        </div>
        </>}
      </section>
    </div>
    {hasScene&&<><div className={s.cutawayReadout} hidden={surfaceMode} aria-live="polite"><span className={s.cutawayEyebrow}>INSPECT</span>{pickedLog?<span>{pickedLog.label}</span>:selected?<span>Water-table depth {selected.depthFeet.join("–")} ft · thickness {selected.thicknessFeet.join("–")} ft · outer range {selected.shallowMeters.toFixed(1)}–{selected.deepMeters.toFixed(1)} m.</span>:<span>Select a column or blue range to read its source.</span>}</div>
    <div className={s.areaTools} hidden={surfaceMode}>
      <details className={s.areaAppearance}><summary>View settings</summary><div className={s.areaAppearanceGrid}>
        <p className={s.muted}>High-detail surface tiles refresh for the visible part of this fixed slice as you zoom. Optional smoothing changes only how pixels are drawn. Recorded well and aquifer values are unchanged.</p>
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
