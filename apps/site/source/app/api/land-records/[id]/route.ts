import { decodeLandObject, filterLandRecords, landRecords } from "../../../land-records";
import { ownedLandTransfer } from "../../../land-records-server";
import { intakeFailure,intakeHeaders,IntakeError,intakeUser,submissionReviews } from "../../../data-intake-server";
export const dynamic="force-dynamic";
export async function GET(request:Request,context:{params:Promise<{id:string}>}){
  try{
    const user=await intakeUser(),{id}=await context.params;const {row,transfer}=await ownedLandTransfer(id,user);
    const params=new URL(request.url).searchParams,records=landRecords(transfer);
    let page;try{page=filterLandRecords(records,params);}catch(error){throw new IntakeError((error as Error).message);}
    const object=params.get("object");
    if(object){
      if([...params.keys()].length!==1||!Object.hasOwn(transfer.objects,object))throw new IntakeError("Original evidence object not found.",404);
      const raw=decodeLandObject(transfer.objects[object]);
      return new Response(new Uint8Array(raw).buffer,{headers:{...intakeHeaders,"Content-Type":"application/octet-stream","Content-Length":String(raw.length),"Content-Disposition":`attachment; filename="land-evidence-${object.slice(7)}.bin"`,"Content-Security-Policy":"sandbox; default-src 'none'","Referrer-Policy":"no-referrer"}});
    }
    const record=params.get("record");if(record&&!records.some(r=>r.record_digest===record))throw new IntakeError("Record not found.",404);
    const evidence=record?transfer.captures.flatMap(c=>c.evidence.filter(e=>e.record_digest===record).map(e=>({...e,coverage:c.candidate.coverage}))):[];
    const {ownerKey:_owner,objectKey:_object,...submission}=row;
    return Response.json({...page,submission,summary:{uniqueRecords:records.length,captures:transfer.captures.length,bytes:row.fileBytes,sources:[...new Set(records.map(r=>r.source_id))],counties:[...new Set(records.map(r=>r.county??"Unknown"))].sort(),kinds:[...new Set(records.map(r=>r.instrument_type))].sort(),start:records[0].event_date,end:records.at(-1)!.event_date,transferDigest:transfer.transfer_digest},selected:record?records.find(r=>r.record_digest===record):null,evidence,reviews:await submissionReviews(id),canReview:user.steward,integrity:"VERIFIED",normalizationReview:"PENDING",sourceAdmission:"PENDING",releaseState:"UNRELEASED",publicRecords:0},{headers:intakeHeaders});
  }catch(error){return intakeFailure(error);}
}
