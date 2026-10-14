import { DatabaseSync } from 'node:sqlite';
import { createHash, randomBytes, scryptSync, timingSafeEqual, createCipheriv, createDecipheriv } from 'node:crypto';
import { mkdirSync, lstatSync, chmodSync } from 'node:fs';
import { join } from 'node:path';

export const digest = value => createHash('sha256').update(value).digest('hex');
export const token = () => randomBytes(32).toString('base64url');
const fail = code => { throw new Error(code); };
export function matchesToken(value, expected) {
  if (typeof value !== 'string' || !/^[A-Za-z0-9_-]{43}$/.test(value) || !/^[a-f0-9]{64}$/.test(expected ?? '')) return false;
  return timingSafeEqual(Buffer.from(digest(value),'hex'),Buffer.from(expected,'hex'));
}
const passwordHash = password => {
  const salt = randomBytes(16).toString('hex');
  return `${salt}:${scryptSync(password,salt,32).toString('hex')}`;
};
const passwordMatches = (password, encoded) => {
  const [salt, hash] = encoded.split(':');
  return timingSafeEqual(scryptSync(password,salt,32),Buffer.from(hash,'hex'));
};
const safeDirectory = directory => {
  try { mkdirSync(directory,{mode:0o700}); } catch (error) { if(error.code !== 'EEXIST') throw error; }
  const info = lstatSync(directory);
  if (!info.isDirectory() || info.isSymbolicLink() || info.uid !== process.getuid()) fail('STORAGE_UNSAFE');
  chmodSync(directory,0o700);
};
const USERNAME = /^[a-z0-9][a-z0-9_-]{2,63}$/;

/** One process owns a connection for its lifetime. Never use WAL on this shared volume. */
export class PcAiStore {
  constructor({root,role,key,clock=Date.now}) {
    if (!['preview','published','test'].includes(role) || !/^[A-Za-z0-9_-]{43}$/.test(key)) fail('STORAGE_CONFIG_INVALID');
    const rootInfo = lstatSync(root);
    if (!rootInfo.isDirectory() || rootInfo.isSymbolicLink()) fail('STORAGE_UNSAFE');
    const parent = join(root,'kfm-pc-ai-v1'); safeDirectory(parent);
    const directory = join(parent,role); safeDirectory(directory);
    const file = join(directory,'accounts-jobs.sqlite');
    try {
      const info = lstatSync(file);
      if (!info.isFile() || info.isSymbolicLink() || info.nlink !== 1 || info.uid !== process.getuid() || info.size>32*1024*1024) fail('STORAGE_UNSAFE');
    } catch(error) { if(error.code !== 'ENOENT') throw error; }
    this.clock=clock; this.key=Buffer.from(key,'base64url'); this.db=new DatabaseSync(file);
    try {
      chmodSync(file,0o600);
      if(this.db.prepare('PRAGMA page_size').get().page_size!==4096)fail('STORAGE_PAGE_SIZE_UNQUALIFIED');
      this.db.exec('PRAGMA busy_timeout=1000; PRAGMA journal_mode=DELETE; PRAGMA synchronous=FULL; PRAGMA foreign_keys=ON; PRAGMA locking_mode=EXCLUSIVE; PRAGMA max_page_count=8192; BEGIN EXCLUSIVE; COMMIT;');
      this.db.exec(`CREATE TABLE IF NOT EXISTS control (id INTEGER PRIMARY KEY CHECK(id=1),schema_version INTEGER NOT NULL,key_digest TEXT NOT NULL,worker_at INTEGER NOT NULL DEFAULT 0,worker_ready INTEGER NOT NULL DEFAULT 0);
        CREATE TABLE IF NOT EXISTS accounts (id TEXT PRIMARY KEY,username TEXT UNIQUE NOT NULL,password TEXT,disabled INTEGER NOT NULL DEFAULT 0,invite_hash TEXT,invite_until INTEGER,created INTEGER NOT NULL);
        CREATE TABLE IF NOT EXISTS sessions (hash TEXT PRIMARY KEY,account TEXT NOT NULL REFERENCES accounts(id),expires INTEGER NOT NULL);
        CREATE TABLE IF NOT EXISTS attempts (username TEXT NOT NULL,at INTEGER NOT NULL);
        CREATE INDEX IF NOT EXISTS attempts_at ON attempts(at);
        CREATE TABLE IF NOT EXISTS jobs (id TEXT PRIMARY KEY,account TEXT NOT NULL REFERENCES accounts(id),state TEXT NOT NULL,created INTEGER NOT NULL,deadline INTEGER NOT NULL,lease_hash TEXT,lease_until INTEGER,payload TEXT,result TEXT);
        CREATE INDEX IF NOT EXISTS jobs_account ON jobs(account,created);`);
      this.db.prepare('INSERT OR IGNORE INTO control(id,schema_version,key_digest) VALUES(1,1,?)').run(digest(this.key));
      const control=this.db.prepare('SELECT * FROM control WHERE id=1').get();
      if(control.schema_version!==1 || control.key_digest!==digest(this.key)) fail('STORAGE_IDENTITY_MISMATCH');
      if(this.db.prepare('PRAGMA integrity_check').get().integrity_check!=='ok') fail('STORAGE_INTEGRITY_HOLD');
    } catch(error) { this.db.close(); throw error; }
  }
  close(){this.db.close();}
  seal(value){
    const iv=randomBytes(12),cipher=createCipheriv('aes-256-gcm',this.key,iv);
    const data=Buffer.concat([cipher.update(JSON.stringify(value),'utf8'),cipher.final()]);
    return Buffer.concat([iv,cipher.getAuthTag(),data]).toString('base64url');
  }
  open(value){
    const bytes=Buffer.from(value,'base64url'),cipher=createDecipheriv('aes-256-gcm',this.key,bytes.subarray(0,12));
    cipher.setAuthTag(bytes.subarray(12,28));
    return JSON.parse(Buffer.concat([cipher.update(bytes.subarray(28)),cipher.final()]).toString('utf8'));
  }
  transaction(work){
    this.db.exec('BEGIN IMMEDIATE');
    try{const result=work();this.db.exec('COMMIT');return result;}
    catch(error){this.db.exec('ROLLBACK');throw error;}
  }
  cleanup(){
    const now=this.clock();
    this.db.prepare("UPDATE jobs SET state='expired',payload=NULL,result=NULL,lease_hash=NULL WHERE state IN ('queued','running') AND (deadline<=? OR (state='running' AND lease_until<=?))").run(now,now);
    this.db.prepare('UPDATE jobs SET payload=NULL,result=NULL WHERE created<=?').run(now-86400000);
    this.db.prepare('DELETE FROM jobs WHERE created<=?').run(now-30*86400000);
    this.db.prepare('DELETE FROM sessions WHERE expires<=?').run(now);
    this.db.prepare('DELETE FROM attempts WHERE at<=?').run(now-3600000);
  }
  invite(username){
    if(typeof username!=='string'||!USERNAME.test(username)) fail('INVALID_USERNAME');
    return this.transaction(()=>{
      if(this.db.prepare('SELECT COUNT(*) AS n FROM accounts').get().n>=50) fail('ACCOUNT_LIMIT');
      if(this.db.prepare('SELECT 1 FROM accounts WHERE username=?').get(username)) fail('ACCOUNT_EXISTS');
      const invitation=token();
      this.db.prepare('INSERT INTO accounts(id,username,invite_hash,invite_until,created) VALUES(?,?,?,?,?)').run(token(),username,digest(invitation),this.clock()+86400000,this.clock());
      return {username,invitation,expiresInSeconds:86400};
    });
  }
  authenticate(username,password,invitation=null){
    if(typeof username!=='string' || !USERNAME.test(username) || typeof password!=='string' || password.length<14 || Buffer.byteLength(password)>128 || /[\x00-\x1f\x7f]/.test(password)) fail('SIGN_IN_DENIED');
    this.cleanup();
    const now=this.clock();
    if(this.db.prepare('SELECT COUNT(*) AS n FROM attempts WHERE at>?').get(now-60000).n>=30 || this.db.prepare('SELECT COUNT(*) AS n FROM attempts WHERE username=? AND at>?').get(username,now-900000).n>=5) fail('SIGN_IN_RATE_LIMIT');
    this.db.prepare('INSERT INTO attempts VALUES(?,?)').run(username,now);
    const account=this.db.prepare('SELECT * FROM accounts WHERE username=?').get(username);
    if(!account || account.disabled) { scryptSync(password,'kfm-pc-dummy-salt',32); fail('SIGN_IN_DENIED'); }
    if(invitation!==null){
      if(account.password || account.invite_until<=now || !matchesToken(invitation,account.invite_hash)) fail('SIGN_IN_DENIED');
      this.db.prepare('UPDATE accounts SET password=?,invite_hash=NULL,invite_until=NULL WHERE id=?').run(passwordHash(password),account.id);
    }else if(!account.password || !passwordMatches(password,account.password)) fail('SIGN_IN_DENIED');
    const session=token();
    this.db.prepare('INSERT INTO sessions VALUES(?,?,?)').run(digest(session),account.id,now+14400000);
    return {session,username:account.username};
  }
  account(session){
    if(typeof session!=='string' || !/^[A-Za-z0-9_-]{43}$/.test(session)) return null;
    return this.db.prepare('SELECT a.id,a.username FROM sessions s JOIN accounts a ON a.id=s.account WHERE s.hash=? AND s.expires>? AND a.disabled=0').get(digest(session),this.clock())??null;
  }
  signOut(session){if(typeof session==='string')this.db.prepare('DELETE FROM sessions WHERE hash=?').run(digest(session));}
  revoke(username){
    if(typeof username!=='string'||!USERNAME.test(username))fail('INVALID_USERNAME');
    this.transaction(()=>{
      const account=this.db.prepare('SELECT id FROM accounts WHERE username=?').get(username);
      if(!account)return;
      this.db.prepare('UPDATE accounts SET disabled=1,invite_hash=NULL WHERE id=?').run(account.id);
      this.db.prepare('DELETE FROM sessions WHERE account=?').run(account.id);
      this.db.prepare("UPDATE jobs SET state='cancelled',payload=NULL,result=NULL,lease_hash=NULL WHERE account=?").run(account.id);
    });
  }
  heartbeat(ready){this.db.prepare('UPDATE control SET worker_at=?,worker_ready=? WHERE id=1').run(this.clock(),ready?1:0);}
  availability(){
    const row=this.db.prepare('SELECT worker_at,worker_ready FROM control WHERE id=1').get();
    return {online:row.worker_at>0&&row.worker_at>this.clock()-15000,ready:row.worker_ready===1&&row.worker_at>this.clock()-15000};
  }
  enqueue(account,packet,terminal=null){
    return this.transaction(()=>{
      this.cleanup();
      if(!this.availability().ready)fail('PC_OFFLINE');
      const now=this.clock();
      if(this.db.prepare('SELECT COUNT(*) AS n FROM jobs WHERE account=? AND created>?').get(account,now-3600000).n>=10)fail('USER_RATE_LIMIT');
      if(this.db.prepare("SELECT COUNT(*) AS n FROM jobs WHERE account=? AND state IN ('queued','running')").get(account).n>0)fail('USER_BUSY');
      if(this.db.prepare("SELECT COUNT(*) AS n FROM jobs WHERE state IN ('queued','running')").get().n>=5)fail('QUEUE_FULL');
      const id=token();
      this.db.prepare('INSERT INTO jobs(id,account,state,created,deadline,payload,result) VALUES(?,?,?,?,?,?,?)').run(id,account,terminal?'completed':'queued',now,now+180000,terminal?null:this.seal(packet),terminal?this.seal(terminal):null);
      return id;
    });
  }
  read(id,account){
    this.cleanup();
    const row=this.db.prepare('SELECT * FROM jobs WHERE id=? AND account=?').get(id,account);
    if(!row)return null;
    return {id,state:row.state,created:row.created,deadline:row.deadline,packet:row.payload?this.open(row.payload):null,result:row.result?this.open(row.result):null};
  }
  cancel(id,account){
    const change=this.db.prepare("UPDATE jobs SET state='cancelled',payload=NULL,result=NULL,lease_hash=NULL WHERE id=? AND account=? AND state IN ('queued','running')").run(id,account);
    return change.changes===1;
  }
  claim(){
    return this.transaction(()=>{
      this.cleanup();
      if(!this.availability().ready || this.db.prepare("SELECT 1 FROM jobs WHERE state='running'").get())return null;
      const row=this.db.prepare("SELECT * FROM jobs WHERE state='queued' ORDER BY created,id LIMIT 1").get();
      if(!row)return null;
      const lease=token(),until=Math.min(this.clock()+100000,row.deadline);
      this.db.prepare("UPDATE jobs SET state='running',lease_hash=?,lease_until=? WHERE id=?").run(digest(lease),until,row.id);
      return {id:row.id,lease,leaseUntil:until,packet:this.open(row.payload)};
    });
  }
  leased(id,lease){
    this.cleanup();
    const row=this.db.prepare("SELECT * FROM jobs WHERE id=? AND state='running' AND lease_until>?").get(id,this.clock());
    if(!row || !matchesToken(lease,row.lease_hash))return null;
    return {packet:this.open(row.payload),account:row.account};
  }
  complete(id,lease,result){
    return this.transaction(()=>{
      if(!this.leased(id,lease))fail('LEASE_LOST');
      this.db.prepare("UPDATE jobs SET state='completed',result=?,lease_hash=NULL WHERE id=?").run(this.seal(result),id);
    });
  }
}
