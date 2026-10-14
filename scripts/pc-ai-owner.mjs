import { randomBytes } from 'node:crypto';
import { writeFile, readFile, lstat } from 'node:fs/promises';
import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { token, digest } from '../server/pc-ai-store.mjs';
import { boundedJson } from './pc-ai-worker.mjs';

const [command,file,username,accountRole]=process.argv.slice(2);
if(command==='prepare'){
  if(!file)throw new Error('Supply a new secret file path outside source and deployment assets.');
  const target=resolve(file),root=fileURLToPath(new URL('../',import.meta.url)).replace(/\/$/,'');
  if(target===root||target.startsWith(root+'/'))throw new Error('CONFIG_MUST_BE_OUTSIDE_SOURCE');
  if(username&&!['preview','published'].includes(username))throw new Error('Role must be preview or published');
  const role=username??'published';
  const config={origin:role==='preview'?'https://q9r9beo47t.preview.c38.airoapp.ai':'https://kansasfrontiermatrix.com',workerToken:token(),adminToken:token(),dataKey:randomBytes(32).toString('base64url')};
  await writeFile(target,JSON.stringify({origin:config.origin,adminToken:config.adminToken},null,2)+'\n',{flag:'wx',mode:0o600});
  await writeFile(target+'.worker.secret.json',JSON.stringify({origin:config.origin,workerToken:config.workerToken},null,2)+'\n',{flag:'wx',mode:0o600});
  await writeFile(target+'.hosting.txt',`KFM_PC_ENABLED=true\nKFM_PC_STORAGE_MODE=single-writer-confirmed\nKFM_PC_ROLE=${role}\nKFM_PC_ORIGIN=${config.origin}\nKFM_PC_ADMIN_TOKEN_HASH=${digest(config.adminToken)}\nKFM_PC_WORKER_TOKEN_HASH=${digest(config.workerToken)}\nKFM_PC_DATA_KEY=${config.dataKey}\n`,{flag:'wx',mode:0o600});
  console.info('Created protected local configuration and provider-entry file. No secrets printed, uploaded, or committed.');
}else if(['invite','revoke','activate'].includes(command)){
  if(!file||!username)throw new Error('Supply owner configuration and username.');
  const info=await lstat(file);if(!info.isFile()||info.isSymbolicLink()||info.uid!==process.getuid()||(info.mode&0o077)||info.size>16384)throw new Error('CONFIG_UNSAFE');
  const config=JSON.parse(await readFile(file,'utf8'));
  if(!['https://kansasfrontiermatrix.com','https://q9r9beo47t.preview.c38.airoapp.ai'].includes(config.origin)||!/^[A-Za-z0-9_-]{43}$/.test(config.adminToken))throw new Error('CONFIG_INVALID');
  let body={username,...(command==='invite'&&accountRole?{role:accountRole}:{})};
  if(command==='activate'){
    const activationInfo=await lstat(username);
    if(!activationInfo.isFile()||activationInfo.isSymbolicLink()||activationInfo.uid!==process.getuid()||(activationInfo.mode&0o077)||activationInfo.size>16384)throw new Error('ACTIVATION_FILE_UNSAFE');
    body=JSON.parse(await readFile(username,'utf8'));
  }
  const response=await fetch(config.origin+'/api/pc-ai/'+(command==='activate'?'activate':'admin/'+command),{method:'POST',redirect:'error',signal:AbortSignal.timeout(8000),headers:{Authorization:'Bearer '+config.adminToken,'Content-Type':'application/json'},body:JSON.stringify(body)});
  const result=await boundedJson(response);
  if(command==='invite'){
    const target=resolve(file+'.'+username+'.invitation.txt');
    if(!/^[a-z0-9][a-z0-9_-]{2,63}$/.test(username)||!/^[A-Za-z0-9_-]{43}$/.test(result.invitation))throw new Error('INVITATION_INVALID');
    await writeFile(target,`Username: ${username}\nInvitation: ${result.invitation}\nActivation: sign in as an administrator or steward at ${config.origin}/assistant\nExpires: 24 hours\n`,{flag:'wx',mode:0o600});
    console.info('Invitation saved beside your protected configuration. Deliver it privately yourself.');
  }else console.info(command==='activate'?'Account activated. Sign in using the top Log in button.':'Account revoked; sessions and jobs cancelled.');
}else throw new Error('Usage: pc-ai-owner.mjs prepare <new-secret-path> | invite <config> <username> [researcher|steward|administrator] | activate <config> <protected-activation-json> | revoke <config> <username>');
