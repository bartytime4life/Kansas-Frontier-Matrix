import {prepareTerrain,type TerrainPreparationRequest,type TerrainPreparationReply} from './terrain-preparation-model';
const scope=globalThis as unknown as {onmessage:((event:MessageEvent<TerrainPreparationRequest>)=>void)|null;postMessage:(reply:TerrainPreparationReply,transfer:Transferable[])=>void};
scope.onmessage=event=>{
 const request=event.data;
 try{const result=prepareTerrain(request);scope.postMessage({id:request.id,result},[result.packed.buffer as ArrayBuffer,result.eligible.buffer as ArrayBuffer]);}
 catch{scope.postMessage({id:request?.id,error:'This landscape could not be prepared. Source readings and continuous terrain remain available.'},[]);}
};
