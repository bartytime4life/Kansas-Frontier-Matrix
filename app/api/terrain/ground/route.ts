import {localGroundRuntime} from "../../../../server/local-data.mjs";
export async function GET(request:Request){return localGroundRuntime()(request);}
