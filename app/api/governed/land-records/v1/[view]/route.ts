export const dynamic="force-dynamic";
export async function GET(){return Response.json({outcome:"DENY",reason_code:"LAND_RELEASE_NOT_IMPLEMENTED",records:[]},{status:403,headers:{"Cache-Control":"no-store","X-Content-Type-Options":"nosniff"}});}
