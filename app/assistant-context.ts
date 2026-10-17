import type {SubsurfaceInspection} from './underground-panel';
export type AssistantSelection =
 | {kind:'registry';layerId:string;featureId:string}
 | {kind:'subsurface';tileId:string;recordId:string;intervalIndex:number|null}
 | {kind:'display';title:string;source:string;description:string;time:string};
export type AssistantContext={version:1;frame:number;view:string;layers:string[];selection:AssistantSelection|null};
export type AssistantFocus={context:AssistantContext;title:string;detail:string};
export function sampleAssistantSelection(inspection:SubsurfaceInspection):AssistantSelection|null{
 if(!inspection.tileId)return null;
 const index=inspection.interval?inspection.record.intervals.indexOf(inspection.interval):null;
 if(index===-1)return null;
 return {kind:'subsurface',tileId:inspection.tileId,recordId:inspection.record.id,intervalIndex:index};
}
