import { validVolumeBounds, type AquiferVolume, type VolumeBounds } from "./aquifer-volume";

type Locator = {
  getPitch(): number; getBearing(): number; getProjection(): {type?: unknown} | null | undefined;
  getBounds(): {getWest(): number; getSouth(): number; getEast(): number; getNorth(): number};
  isMoving(): boolean; areTilesLoaded(): boolean; triggerRepaint(): void;
  on(event: string, listener: () => void): unknown; off(event: string, listener: () => void): unknown;
};
type WorkerPort = {
  postMessage(value: {id: number; bounds: VolumeBounds}): void;
  onmessage: ((event: MessageEvent<{id: number; volume?: AquiferVolume; error?: string}>) => void) | null;
  onerror: ((event: ErrorEvent) => unknown) | null;
};
export type AquiferViewSnapshot<Image> = {volume: AquiferVolume; image: Image | null; aquiferState?: "loading" | "ready" | "unavailable"};
export function locatorBounds(map: Pick<Locator,"getBounds">): VolumeBounds {
  const b=map.getBounds();return [b.getWest(),b.getSouth(),b.getEast(),b.getNorth()];
}
const sameBounds=(a:VolumeBounds,b:VolumeBounds)=>a.every((value,index)=>value===b[index]);

/** A selected reference frame/log scene is independent of optional aquifer geometry and imagery. */
export function startAquiferView<Image>(options: {
  map: Locator; worker: WorkerPort | null; sampleSurface: () => Image;
  manual?: boolean; initialSnapshot?: AquiferViewSnapshot<Image> | null; onArea?: (bounds: VolumeBounds | null) => void; onPreview?: (changed: boolean) => void;
  onSnapshot: (snapshot: AquiferViewSnapshot<Image> | null) => void;
  onStatus: (status: string) => void; onSurfaceStatus: (status: string) => void;
  timers?: {set: (callback: () => void, delay: number) => unknown; clear: (handle: unknown) => void};
}) {
  const {map,worker,sampleSurface,onSnapshot,onStatus,onSurfaceStatus}=options;
  const timers=options.timers??{set:(callback:()=>void,delay:number)=>globalThis.setTimeout(callback,delay),clear:(handle:unknown)=>globalThis.clearTimeout(handle as ReturnType<typeof setTimeout>)};
  let serial=0,disposed=false,awaitingLocator=false,requested=false,timeout:unknown,geometryTimeout:unknown,debounce:unknown,capture:(()=>void)|null=null;
  let pending:{id:number;bounds:VolumeBounds;volume:AquiferVolume|null;image:Image|null;aquiferState:"loading"|"ready"|"unavailable"}|null=null;
  const clearCapture=()=>{if(capture)map.off("render",capture);capture=null;timers.clear(timeout);};
  const publish=()=>{if(pending?.volume)onSnapshot({volume:pending.volume,image:pending.image,aquiferState:pending.aquiferState});};
  const unavailable=(message:string)=>{timers.clear(geometryTimeout);if(pending){pending.aquiferState="unavailable";publish();}onStatus(`${message} Independent recorded columns remain available; retry the area to retry aquifer ranges.`);};
  const prepare=()=>{
    if(disposed)return;
    requested=true;awaitingLocator=true;
    let bounds:VolumeBounds;
    try{
      const projection=map.getProjection()?.type;
      if(typeof projection!=="string"){onStatus("Waiting for the map style. Your area request will continue when it is ready.");return;}
      if(Math.abs(map.getPitch())>.1||Math.abs(map.getBearing())>.1||projection!=="mercator"){
        onStatus("Waiting for the map to return to 2D. Your area request will continue when it stops.");return;
      }
      if(map.isMoving()){onStatus("Finishing the map movement, then loading this area…");return;}
      bounds=locatorBounds(map);
    }catch{onStatus("Waiting for the map style. Your area request will continue when it is ready.");return;}
    awaitingLocator=false;
    if(!validVolumeBounds(bounds)){
      requested=false;if(!pending)options.onArea?.(null);
      onStatus("This map is too wide or outside Kansas. Choose Zoom in & explore, or move the map to Kansas.");return;
    }
    requested=false;timers.clear(debounce);clearCapture();timers.clear(geometryTimeout);
    const id=++serial;
    // The empty envelope list is a display extent, never an inferred aquifer or geology.
    const reference:AquiferVolume={bounds,envelopes:[],heldClasses:0,truncated:false,period:"2022–2024"};
    pending={id,bounds,volume:options.manual?reference:null,image:null,aquiferState:worker?"loading":"unavailable"};
    options.onPreview?.(false);options.onArea?.(bounds);if(options.manual)publish();else onSnapshot(null);
    onStatus(worker?"Loading optional aquifer ranges…":"Aquifer preparation is unavailable. Independent recorded columns can still load.");
    onSurfaceStatus("Loading the selected-area map image separately…");
    if(worker){
      try{worker.postMessage({id,bounds});geometryTimeout=timers.set(()=>{if(!disposed&&pending?.id===id&&pending.aquiferState==="loading")unavailable("Aquifer preparation timed out.");},14000);}
      catch{unavailable("Aquifer preparation could not start.");}
    }
    capture=()=>{
      if(disposed||id!==serial||!pending)return;
      try{
        if(map.isMoving()||!map.areTilesLoaded())return;
        if(!sameBounds(locatorBounds(map),pending.bounds)){clearCapture();options.onPreview?.(true);onSurfaceStatus("Map image withheld: the selector has moved away from the selected area.");return;}
        const image=sampleSurface();if(disposed||id!==serial||!pending)return;
        pending.image=image;clearCapture();publish();onSurfaceStatus("Map image matches the selected area.");
      }catch{if(disposed||id!==serial)return;clearCapture();onSurfaceStatus("Map image unavailable. The reference plane and recorded columns remain available.");}
    };
    map.on("render",capture);timeout=timers.set(()=>{if(disposed||id!==serial)return;clearCapture();onSurfaceStatus("Map image unavailable: tiles did not finish. Recorded columns remain available.");},8000);
    map.triggerRepaint();
  };
  if(worker){
    worker.onmessage=({data})=>{
      if(disposed||data.id!==serial||pending?.id!==data.id)return;
      timers.clear(geometryTimeout);
      if(data.volume){
        if(!validVolumeBounds(data.volume.bounds)||!sameBounds(data.volume.bounds,pending.bounds)){unavailable("Aquifer response did not match the selected area; ranges withheld.");return;}
        pending.volume=data.volume;pending.aquiferState="ready";publish();
        onStatus(`${data.volume.envelopes.length} aquifer overlap regions · 2022–2024${data.volume.heldClasses?` · ${data.volume.heldClasses} unbounded/missing classes withheld`:""}${data.volume.truncated?" · partial geometry":""}`);
      }else unavailable(data.error??"Aquifer ranges unavailable.");
    };
    worker.onerror=()=>{if(!disposed)unavailable("Aquifer preparation failed.");};
  }
  const preview=()=>{if(disposed)return;try{options.onPreview?.(pending?!sameBounds(locatorBounds(map),pending.bounds):false);}catch{options.onPreview?.(Boolean(pending));}};
  const invalidate=()=>{
    if(disposed)return;
    if(options.manual){preview();return;}
    awaitingLocator=false;clearCapture();timers.clear(geometryTimeout);pending=null;serial++;timers.clear(debounce);onSnapshot(null);onSurfaceStatus("");onStatus("Locator changed. Preparing the new area when movement stops…");
  };
  const schedule=()=>{
    if(disposed)return;
    if(options.manual){preview();if(requested){timers.clear(debounce);debounce=timers.set(prepare,80);}return;}
    invalidate();debounce=timers.set(prepare,250);
  };
  const locatorReady=()=>{if(disposed||!awaitingLocator)return;timers.clear(debounce);debounce=timers.set(prepare,options.manual?80:250);};
  const stop=()=>{
    if(disposed)return;disposed=true;serial++;pending=null;clearCapture();timers.clear(geometryTimeout);timers.clear(debounce);
    map.off("movestart",invalidate);map.off("moveend",schedule);map.off("resize",schedule);map.off("styledata",locatorReady);map.off("load",locatorReady);map.off("remove",removed);
    if(worker){worker.onmessage=null;worker.onerror=null;}
  };
  const removed=()=>{if(disposed)return;stop();onSnapshot(null);onSurfaceStatus("");onStatus("Map removed. Reopen Underground when it is available.");};
  map.on("movestart",invalidate);map.on("moveend",schedule);map.on("resize",schedule);map.on("styledata",locatorReady);map.on("load",locatorReady);map.on("remove",removed);
  if(options.manual&&options.initialSnapshot){
    const saved=options.initialSnapshot;
    pending={id:serial,bounds:saved.volume.bounds,volume:saved.volume,image:saved.image,aquiferState:saved.aquiferState==="loading"?"unavailable":saved.aquiferState??"ready"};
    publish();preview();onStatus(saved.aquiferState==="loading"?"Selected area retained. Show this area again to retry the interrupted optional aquifer load.":"Selected area retained. Pan the map to preview another area.");
  }else if(!options.manual)prepare();else onStatus("Choose a local area, then show its recorded columns.");
  return Object.assign(stop,{prepare});
}
