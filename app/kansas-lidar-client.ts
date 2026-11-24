import {createNativeReader,readNativeDataset} from './native-lidar-client';
import {lidarViewPath,lidarViewRequestKey,parseLidarAnalysisGrid,parseLidarViewReceipt,type KansasLidarView,type LidarViewQuery,type LidarViewReceipt} from './kansas-lidar-view';
const pause=(signal:AbortSignal)=>new Promise<void>((resolve,reject)=>{const abort=()=>{clearTimeout(timer);reject(signal.reason);},timer=setTimeout(()=>{signal.removeEventListener('abort',abort);resolve();},2000);signal.addEventListener('abort',abort,{once:true});if(signal.aborted)abort();});
/** One canonical view request at a time, then at most two native chunk reads.
 * Complete analysis grid transport is separate from the sparse display LOD. */
export async function readKansasLidarView(query:LidarViewQuery,signal:AbortSignal,onReceipt?:(receipt:LidarViewReceipt)=>void):Promise<KansasLidarView>{
  const reader=createNativeReader(signal,145_000),deadline=Date.now()+120_000;
  try{
    const requestKey=await lidarViewRequestKey(query);reader.signal.throwIfAborted();let receipt:LidarViewReceipt;
    for(;;){const parsed=parseLidarViewReceipt(await reader.read(lidarViewPath(query)),query,requestKey);if(!parsed)throw Error('LiDAR viewport response failed source or query validation.');receipt=parsed;onReceipt?.(receipt);if(receipt.state!=='processing'||Date.now()>=deadline)break;await pause(reader.signal);}
    const prefix='/api/lidar/view/'+receipt.requestKey+'/';
    const points=receipt.points&&query.layers.includes('points')?await readNativeDataset(receipt.points,reader.read,reader.signal,id=>prefix+id):null;
    const rawGrid=receipt.grid&&query.layers.some(l=>l==='surface'||l==='canopy')?await reader.read(prefix+'grid'):null;
    const grid=rawGrid===null?null:parseLidarAnalysisGrid(rawGrid,receipt);if(rawGrid!==null&&!grid)throw Error('Complete LiDAR grid failed method, support or source validation.');
    if(grid&&points){const assets=new Map(points.manifest.source.assets.map(a=>[a.url,a]));for(const a of grid.source.assets){const p=assets.get(a.url);if(p&&((['sha256','bytes','pointCount','project','eptUrl','acquisition','verticalReference','gpsTimeType'] as const).some(key=>p[key]!==a[key])||JSON.stringify(p.coordinateEncodingM)!==JSON.stringify(a.coordinateEncodingM)))throw Error('Point and grid source receipts disagree.');}}
    reader.signal.throwIfAborted();return {receipt,points,grid};
  }catch(error){reader.abort();throw error;}finally{reader.dispose();}
}
