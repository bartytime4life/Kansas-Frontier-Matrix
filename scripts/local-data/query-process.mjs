// Child process: read-only SQLite, no network, no credentials, no arbitrary SQL from IPC.
import {createDatabaseReader} from './database-reader.mjs';
import {LOCAL_DATA_LIMITS} from './protocol.mjs';
import {setPriority} from 'node:os';
try{setPriority(0,10);}catch{}
let read,active=false;
process.on('message',message=>{
 if(message?.kind==='init'&&!read){read=createDatabaseReader({databases:message.databases});process.send?.({ready:true});return;}
 if(!read||active||!Number.isSafeInteger(message?.id))return;
 active=true;
 try{
  const value=read(message.operation);
  if(Buffer.byteLength(JSON.stringify(value))>LOCAL_DATA_LIMITS.replyBytes)throw Object.assign(new Error(),{code:'REPLY_TOO_LARGE'});
  process.send?.({id:message.id,value});
 }catch(error){
  const code=['QUERY_INVALID','DATASET_NOT_READY','REPLY_TOO_LARGE'].includes(error?.code)?error.code:'DATABASE_UNAVAILABLE';
  process.send?.({id:message.id,error:code});
 }finally{active=false;}
});
process.on('disconnect',()=>process.exit(0));
