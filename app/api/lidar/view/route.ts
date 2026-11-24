import {localLidarViewRuntime} from "../../../../server/local-data.mjs";
export async function GET(request:Request){return localLidarViewRuntime()(request);}
