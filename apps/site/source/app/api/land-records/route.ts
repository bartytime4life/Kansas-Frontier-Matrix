import { LAND_SOURCE_ID, LAND_LIMIT, landRecords, validateLandTransfer, LAND_SOURCES } from "../../land-records";
import { boundedForm, intakeFailure, intakeHeaders, IntakeError, intakeStore, intakeUser, sameOrigin, sha256, submissionColumns, withSubmissionUpload } from "../../data-intake-server";
import type { Submission } from "../../data-intake";
export const dynamic="force-dynamic";
export async function GET(request: Request) {
  try {
    const user=await intakeUser(),{db}=intakeStore();const p=new URL(request.url).searchParams;
    if([...p.keys()].some(k=>!["before","scope"].includes(k)||p.getAll(k).length!==1))throw new IntakeError("Invalid submission filter.");
    const queue=p.get("scope")==="review";if(queue&&!user.steward)throw new IntakeError("This review queue is available to assigned stewards.",403);
    const cursor=p.get("before");if(cursor&&!/^\d{4}-\d\d-\d\dT[\d:.]+Z\|[0-9a-f-]{36}$/.test(cursor))throw new IntakeError("Invalid page cursor.");
    const [when,id]=cursor?.split("|")??[];
    const clauses=["source_id = ?",...(queue?[]:["owner_key = ?"]),...(cursor?["(created_at,id) < (?,?)"]:[])];
    const args=[LAND_SOURCE_ID,...(queue?[]:[user.key]),...(cursor?[when,id]:[])];
    const rows=(await db.prepare(`SELECT ${submissionColumns} FROM data_submissions WHERE ${clauses.join(" AND ")} ORDER BY created_at DESC,id DESC LIMIT 21`).bind(...args).all<Submission>()).results;
    const items=rows.slice(0,20),last=items.at(-1);
    return Response.json({items,nextCursor:rows.length>20&&last?`${last.createdAt}|${last.id}`:null,publicRecords:0,releaseState:"UNRELEASED"},{headers:intakeHeaders});
  }catch(error){return intakeFailure(error);}
}
export async function POST(request:Request){
  try{
    sameOrigin(request);const user=await intakeUser(),{db,bucket}=intakeStore();
    return await withSubmissionUpload({db,bucket},user.key,async({id,objectKey:key,save})=>{
      const form=await boundedForm(request);
      if([...form.keys()].some(k=>!["file","permission","title"].includes(k)||form.getAll(k).length!==1)||form.get("permission")!=="yes")throw new IntakeError("Confirm that you may share this bundle for private review.");
      const file=form.get("file");if(!file||typeof file==="string"||!file.name.endsWith(".json")||file.size<1||file.size>LAND_LIMIT)throw new IntakeError("Choose a pipeline JSON bundle no larger than 10 MiB.",413);
      const title=form.get("title");if(typeof title!=="string"||title.trim().length<3||title.length>160||/[\x00-\x1f\x7f]/.test(title))throw new IntakeError("Give the bundle a title of 3–160 characters.");
      const bytes=await file.arrayBuffer();let transfer;try{transfer=await validateLandTransfer(new Uint8Array(bytes));}catch(error){throw new IntakeError((error as Error).message);}
      const hash=await sha256(bytes),records=landRecords(transfer);
      const prior=await db.prepare("SELECT id FROM data_submissions WHERE owner_key = ? AND source_id = ? AND file_sha256 = ? ORDER BY created_at LIMIT 1").bind(user.key,LAND_SOURCE_ID,hash).first<{id:string}>();
      if(prior)return Response.json({id:prior.id,replayed:true,records:records.length,releaseState:"UNRELEASED"},{headers:intakeHeaders});
      const now=new Date().toISOString();
      await save(bytes,db.prepare("INSERT INTO data_submissions (id,owner_key,owner_name,title,source_id,source_url,description,license,sensitivity,start_date,end_date,file_name,file_bytes,file_sha256,object_key,status,version,created_at,updated_at) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,'submitted',1,?,?)").bind(id,user.key,user.name,title.trim(),LAND_SOURCE_ID,LAND_SOURCES[records[0].source_id].href,`${records.length} unique candidate versions in ${transfer.captures.length} source captures. Transfer ${transfer.transfer_digest}. Integrity only; normalization, rights, sensitivity, source admission and release remain pending.`,"Unknown; source-specific rights review pending","restricted",records[0].event_date,records.at(-1)!.event_date,"land-review-bundle.json",bytes.byteLength,hash,key,now,now));
      return Response.json({id,records:records.length,releaseState:"UNRELEASED"},{status:201,headers:intakeHeaders});
    });
  }catch(error){return intakeFailure(error);}
}
