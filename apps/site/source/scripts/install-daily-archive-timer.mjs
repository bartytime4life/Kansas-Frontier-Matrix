#!/usr/bin/env node
import { realpathSync } from "node:fs";
import { mkdir, readFile, writeFile, lstat, realpath } from "node:fs/promises";
import { homedir } from "node:os";
import { spawnSync } from "node:child_process";
import path from "node:path";
import { pathToFileURL } from "node:url";
export function archiveUnits(node,site) {
  for(const value of [node,site])if(!path.isAbsolute(value)||/[\n\r"\\%]/.test(value))throw new Error("UNSAFE_UNIT_PATH");
  return {
    "kfm-daily-archive.service": `[Unit]\nDescription=Retain daily Kansas source snapshots\nRequires=kfm-explorer-local.service\nAfter=kfm-explorer-local.service\n\n[Service]\nType=oneshot\nExecStart="${node}" "${site}/scripts/capture-daily-archive.mjs"\nTimeoutStartSec=30min\nSuccessExitStatus=2\nNoNewPrivileges=true\n`,
    "kfm-daily-archive.timer": "[Unit]\nDescription=Daily Kansas archive capture and retry\n\n[Timer]\nOnCalendar=*-*-* 23:15:00 UTC\nOnCalendar=*-*-* 23:45:00 UTC\nPersistent=true\nUnit=kfm-daily-archive.service\n\n[Install]\nWantedBy=timers.target\n",
  };
}
export async function installTimer(site=path.join(homedir(),"Projects/KFM-Explorer-Site-current"),apply=false) {
  const resolved=await realpath(site);const hosting=JSON.parse(await readFile(path.join(resolved,".openai/hosting.json"),"utf8"));
  if(hosting.project_id!=="appgprj_6aa0b1c41bc08191bfd86003920f1631")throw new Error("WRONG_SITE");
  const runner=await lstat(path.join(resolved,"scripts/capture-daily-archive.mjs"));if(!runner.isFile())throw new Error("RUNNER_MISSING");
  const directory=path.join(homedir(),".config/systemd/user");const units=archiveUnits(process.execPath,site);
  for(const [name,content] of Object.entries(units)){
    try {const info=await lstat(path.join(directory,name));const existing=await readFile(path.join(directory,name),"utf8");if(!info.isFile()||info.isSymbolicLink()||![content,content.replace("SuccessExitStatus=2\n","")].includes(existing))throw new Error("EXISTING_UNIT_DIFFERS");}
    catch(error){if(error.code!=="ENOENT")throw error;}
  }
  if(apply){
    await mkdir(directory,{recursive:true,mode:0o700});
    for(const [name,content] of Object.entries(units))await writeFile(path.join(directory,name),content,{mode:0o600});
    for(const args of [["--user","daemon-reload"],["--user","enable","--now","kfm-daily-archive.timer"]]){const result=spawnSync("systemctl",args,{stdio:"inherit"});if(result.status!==0)throw new Error("SYSTEMD_SETUP_FAILED");}
  }
  return {applied:apply,site,directory,units};
}
if(process.argv[1]&&import.meta.url===pathToFileURL(realpathSync(process.argv[1])).href){
 const args=process.argv.slice(2);if(args.some(arg=>arg!=="--apply")||args.length>1)throw new Error("USAGE: --apply");
 console.log(JSON.stringify(await installTimer(undefined,args[0]==="--apply")));
}
