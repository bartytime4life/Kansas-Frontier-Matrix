import type {SubsurfaceInspection} from './underground-panel';
import type {MapSnapshot} from './workspace-model';
export type AssistantSelection =
 | {kind:'registry';layerId:string;featureId:string}
 | {kind:'subsurface';tileId:string;recordId:string;intervalIndex:number|null}
 | {kind:'knowledge';recordId:string}
 | {kind:'display';title:string;source:string;description:string;time:string};
export type AssistantContext={version:1;frame:number;view:string;layers:string[];selection:AssistantSelection|null;surface?:string;filters?:{evidence:string;temporalMode:string};comparison?:{frameA:number;frameB:number}};
export type AssistantFocus={context:AssistantContext;title:string;detail:string};
/** Staging never projects private or release-held sample selectors into AI. */
export function sampleAssistantSelection(_inspection:SubsurfaceInspection):AssistantSelection|null{return null;}
export function snapshotAssistantFocus(snapshot:MapSnapshot,mode:'reports'|'stories'):AssistantFocus{
 const withheld=snapshot.camera.center==='WITHHELD_BROWSER_LOCATION';
 return {title:mode==='reports'?'Report map context':'Story map context',detail:withheld?'Private location-derived snapshot details are withheld.':'Captured map layers and time only; private draft text is not sent.',
 context:{version:1,frame:snapshot.temporalSweep?.frame??snapshot.committedTime.start,view:snapshot.representation,layers:withheld?[]:snapshot.visibleLayers.slice(0,14).map(layer=>layer.id),selection:null,surface:mode,
 ...(withheld?{}:{filters:{evidence:snapshot.evidenceFilter??'ALL',temporalMode:snapshot.temporalSweep?.mode??'snapshot'},...(snapshot.comparison?{comparison:{frameA:snapshot.comparison.timeA,frameB:snapshot.comparison.timeB}}:{})})}};
}
