import {scheduledProfiles} from "../../../api-connections-runtime/connections.mjs";
import {connectionWorker,connectionOwner,connectionSameOrigin,connectionEnvironment,connectionStore,requireConnectionCapture} from "../../../api-connection-host";
export const dynamic="force-dynamic";
export async function POST(request:Request){
 const headers={"Cache-Control":"no-store","X-Content-Type-Options":"nosniff"};
 if(new URL(request.url).search||request.headers.get("content-length")&&!["0"].includes(request.headers.get("content-length")!))return Response.json({error:"Fixed configured profiles only."},{status:400,headers});
 if(!connectionWorker(request)&&!(connectionSameOrigin(request)&&await connectionOwner(request)))return Response.json({error:"Owner or capture-worker access required."},{status:401,headers});
 try{await requireConnectionCapture();return Response.json(await scheduledProfiles(await connectionStore(),{env:connectionEnvironment(),signal:request.signal}),{headers});}catch{return Response.json({error:"Capture profiles or host setup are held."},{status:409,headers});}
}
