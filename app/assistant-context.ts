import type {SubsurfaceInspection} from './underground-panel';
import type {MapSnapshot} from './workspace-model';
export type AssistantSelection =
 | {kind:'registry';layerId:string;featureId:string}
 | {kind:'subsurface';tileId:string;recordId:string;intervalIndex:number|null}
 | {kind:'knowledge';recordId:string}
 | {kind:'display';title:string;source:string;description:string;time:string};
export type AssistantContext={version:1;frame:number;view:string;layers:string[];selection:AssistantSelection|null;surface?:string;filters?:{evidence:string;temporalMode:string};comparison?:{frameA:number;frameB:number}};
export type AssistantFocus={context:AssistantContext;title:string;detail:string};
export function sampleAssistantSelection(inspection:SubsurfaceInspection):AssistantSelection|null{
 if(!inspection.tileId)return null;
 const index=inspection.interval?inspection.record.intervals.indexOf(inspection.interval):null;
 if(index===-1)return null;
 return {kind:'subsurface',tileId:inspection.tileId,recordId:inspection.record.id,intervalIndex:index};
}
export function snapshotAssistantFocus(snapshot:MapSnapshot,mode:'reports'|'stories'):AssistantFocus{
 const withheld=snapshot.camera.center==='WITHHELD_BROWSER_LOCATION';
 return {title:mode==='reports'?'Report map context':'Story map context',detail:withheld?'Private location-derived snapshot details are withheld.':'Captured map layers and time only; private draft text is not sent.',
 context:{version:1,frame:snapshot.temporalSweep?.frame??snapshot.committedTime.start,view:snapshot.representation,layers:withheld?[]:snapshot.visibleLayers.slice(0,14).map(layer=>layer.id),selection:null,surface:mode,
 ...(withheld?{}:{filters:{evidence:snapshot.evidenceFilter??'ALL',temporalMode:snapshot.temporalSweep?.mode??'snapshot'},...(snapshot.comparison?{comparison:{frameA:snapshot.comparison.timeA,frameB:snapshot.comparison.timeB}}:{})})}};
}
