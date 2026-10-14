import { LAND_LIMIT, LAND_SOURCE_ID, validateLandTransfer } from "./land-records";
import { intakeStore, intakeUser, ownedSubmission, IntakeError, sha256 } from "./data-intake-server";
export async function ownedLandTransfer(id: string, user: Awaited<ReturnType<typeof intakeUser>>) {
  const row = await ownedSubmission(id,user);
  if(row.sourceId!==LAND_SOURCE_ID)throw new IntakeError("Land submission not found.",404);
  const object=await intakeStore().bucket.get(row.objectKey);
  if(!object||object.size!==row.fileBytes||object.size>LAND_LIMIT)throw new IntakeError("Original bundle is unavailable or changed. Please export it again.",409);
  const reader=object.body.getReader(),chunks:Uint8Array[]=[];let length=0;
  for(;;){const {done,value}=await reader.read();if(done)break;length+=value.length;if(length>LAND_LIMIT){await reader.cancel();throw new IntakeError("Land bundle exceeds 10 MiB.",413);}chunks.push(value);}
  const bytes=new Uint8Array(length);let offset=0;for(const chunk of chunks){bytes.set(chunk,offset);offset+=chunk.length;}
  if(length!==row.fileBytes||await sha256(bytes.buffer)!==row.fileSha256)throw new IntakeError("Original bundle integrity failed.",409);
  try{return {row,transfer:await validateLandTransfer(bytes)};}catch(error){throw new IntakeError((error as Error).message,409);}
}
