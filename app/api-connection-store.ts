import {archiveStorage, archiveHash, type ArchiveDb, type ArchiveBucket} from "./daily-archive-store";
type Plan={id:string;sourceId:string;slot:number;limitBytes:number};
type Capture={bytes:Uint8Array;receipt:Record<string,unknown>};
const MAX_ARCHIVE=80_000_000_000;
export class SitesConnectionStore {
 constructor(readonly db:ArchiveDb,readonly bucket:ArchiveBucket){}
 async status(){const storage=await archiveStorage(this.db);await this.db.prepare("SELECT id FROM api_connection_receipts LIMIT 1").first();return {paused:storage.paused,usedBytes:storage.used,limitBytes:Math.min(storage.budget,MAX_ARCHIVE),configured:true,state:storage.paused?"paused":"ready-for-owner-capture"};}
 async claim(at:number){const token=crypto.randomUUID(),start=new Date(at).toISOString(),end=new Date(at+180000).toISOString();const s=await this.status();if(s.paused)return null;const result=await this.db.batch([this.db.prepare("INSERT INTO daily_archive_lock(id,token,expires_at) VALUES(1,?,?) ON CONFLICT(id) DO UPDATE SET token=excluded.token,expires_at=excluded.expires_at WHERE expires_at < ?").bind(token,end,start)]);return result[0].meta?.changes===1?token:null;}
 async fenced(token:string){if(!await this.db.prepare("SELECT token FROM daily_archive_lock WHERE id=1 AND token=? AND expires_at>?").bind(token,new Date().toISOString()).first())throw new Error("LEASE_LOST");if((await this.status()).paused)throw new Error("PIPELINE_PAUSED");}
 async due(plan:Plan,token:string){await this.fenced(token);return !await this.db.prepare("SELECT id FROM daily_archive_captures WHERE id=?").bind(plan.id).first();}
 async reserve(plan:Plan,token:string){await this.fenced(token);const s=await this.status();const amount=plan.limitBytes+16384;if(s.usedBytes+amount>s.limitBytes)throw new Error("ARCHIVE_LIMIT_REACHED");await this.db.prepare("INSERT INTO daily_archive_captures(id,day,feed,attempt,status,started_at,bytes) SELECT ?,?,?,1,'api-running',?,? WHERE EXISTS(SELECT 1 FROM daily_archive_lock WHERE id=1 AND token=? AND expires_at>?)").bind(plan.id,new Date(plan.slot).toISOString().slice(0,10),"api:"+plan.sourceId+":"+plan.id,new Date().toISOString(),amount,token,new Date().toISOString()).run();await this.fenced(token);return amount;}
 async save(plan:Plan,capture:Capture,token:string,reservation:number){
  if(capture.bytes.length>plan.limitBytes||capture.receipt.captureId!==plan.id||await archiveHash(capture.bytes)!==capture.receipt.sha256)throw new Error("CAPTURE_INTEGRITY_FAILED");
  const receipt=JSON.stringify(capture.receipt),accounted=capture.bytes.length+new TextEncoder().encode(receipt).length+8192;
  if(accounted>reservation)throw new Error("ARCHIVE_LIMIT_REACHED");await this.fenced(token);
  const key="api-connections/v1/"+plan.id+"/"+capture.receipt.sha256+".json";
  // Reserve full amount before R2; interrupted writes remain fully accounted.
  await this.db.prepare("UPDATE daily_archive_captures SET object_key=?,sha256=? WHERE id=? AND status='api-running'").bind(key,capture.receipt.sha256,plan.id).run();
  await this.bucket.put(key,capture.bytes,{httpMetadata:{contentType:"application/json"}});
  const object=await this.bucket.get(key);if(!object||object.size!==capture.bytes.length||await archiveHash(new Uint8Array(await object.arrayBuffer()))!==capture.receipt.sha256)throw new Error("CAPTURE_INTEGRITY_FAILED");
  await this.fenced(token);
  const result=await this.db.batch([this.db.prepare("INSERT INTO api_connection_receipts(id,source_id,slot,receipt) SELECT ?,?,?,? WHERE EXISTS(SELECT 1 FROM daily_archive_lock WHERE id=1 AND token=? AND expires_at>?)").bind(plan.id,plan.sourceId,plan.slot,receipt,token,new Date().toISOString()),this.db.prepare("UPDATE daily_archive_captures SET status='api-quarantined',finished_at=?,bytes=? WHERE id=? AND EXISTS(SELECT 1 FROM daily_archive_lock WHERE id=1 AND token=? AND expires_at>?)").bind(new Date().toISOString(),accounted,plan.id,token,new Date().toISOString())]);
  if(result.some(r=>r.meta?.changes!==1))throw new Error("LEASE_LOST");
 }
 async failure(plan:Plan,token:string,code:string,reservation:number){if(code!=="API_CAPTURE_HELD"||reservation<0)throw new Error("CAPTURE_FAILURE_REJECTED");await this.fenced(token);await this.db.prepare("UPDATE daily_archive_captures SET status='api-failed',message='API_CAPTURE_HELD',finished_at=? WHERE id=? AND status='api-running'").bind(new Date().toISOString(),plan.id).run();}
 async release(token:string){await this.db.prepare("DELETE FROM daily_archive_lock WHERE id=1 AND token=?").bind(token).run();}
 async lastAttempt(sourceId:string){const r=await this.db.prepare("SELECT MAX(started_at) AS stamp FROM daily_archive_captures WHERE feed LIKE ?").bind("api:"+sourceId+":%").first<{stamp:string|null}>();return r?.stamp?Date.parse(r.stamp):0;}
 async list(){return (await this.db.prepare("SELECT receipt FROM api_connection_receipts ORDER BY slot DESC,id DESC LIMIT 50").all<{receipt:string}>()).results.map(row=>JSON.parse(row.receipt));}
 async read(id:string){if(!/^[a-f0-9]{64}$/.test(id))throw new Error("CAPTURE_NOT_FOUND");const row=await this.db.prepare("SELECT c.object_key,c.sha256,r.receipt FROM daily_archive_captures c JOIN api_connection_receipts r ON r.id=c.id WHERE c.id=? AND c.status='api-quarantined'").bind(id).first<{object_key:string;sha256:string;receipt:string}>();if(!row)throw new Error("CAPTURE_NOT_FOUND");const receipt=JSON.parse(row.receipt);const object=await this.bucket.get(row.object_key);if(!object||object.size!==receipt.byteLength||object.size>4000000)throw new Error("CAPTURE_INTEGRITY_FAILED");const bytes=new Uint8Array(await object.arrayBuffer());if(await archiveHash(bytes)!==row.sha256||row.sha256!==receipt.sha256)throw new Error("CAPTURE_INTEGRITY_FAILED");return {bytes,receipt};}
}
