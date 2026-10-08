#!/usr/bin/env python3
"""Owner-operated loopback download control. Candidate bytes never become map layers."""
from __future__ import annotations
import argparse
import fcntl
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import secrets
import shutil
import sys
import threading
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit

REPO=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(REPO))
from connectors.google.earth_engine.download import SPECS, MAX_BYTES, capture, selection
from tools.local_data.acquisition import validate_root, save_state
from tools.local_data.candidate_capture import create_candidate, write_candidate
from tools.local_data.file_io import check_directory, read_regular, hash_regular, write_new
from tools.local_data.manage import utc_now
from tools.local_data.earth_engine_auth import SignIn, credentials as ee_credentials
from tools.local_data.library import LocalLibrary

PORT=8769
ORIGINS={"http://127.0.0.1:4173","https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site"}
ID=re.compile(r"[a-f0-9]{32}\Z")
TERMINAL={"downloaded","failed","cancelled","interrupted"}

def object_json(path):
    return json.loads(read_regular(path,8*1024*1024))

class Downloads:
    def __init__(self,root):
        validate_root(root)
        self.root=root
        self.work=root/"data/work/earth-engine-downloads"
        self.raw=root/"data/raw/earth-engine"
        self.receipts=root/"data/receipts/ingest/earth-engine"
        for p in (self.work/"jobs",self.raw,self.receipts): check_directory(p,create=True)
        self.jobs={}
        self.lock=threading.RLock()
        self.signin=SignIn(self.work)
        self.cancel_event=threading.Event()
        self.active=None
        self.token=secrets.token_urlsafe(32)
        self.library=LocalLibrary(root)
        files=list((self.work/"jobs").glob("*.json"))
        if len(files)>1000: raise ValueError("JOB_HISTORY_LIMIT")
        for p in files:
            if not ID.fullmatch(p.stem): raise ValueError("INVALID_JOB_FILE")
            job=object_json(p)
            if job.get("state") not in TERMINAL:
                job.update(state="interrupted",reason="WORKER_RESTARTED",updatedAt=utc_now())
                save_state(p,job)
            self.jobs[p.stem]=job

    def configuration(self):
        config=self.work/"config.json"
        return object_json(config) if config.exists() else {}

    def health(self):
        project=self.configuration().get("project")
        credentials=self.work/"credentials.json"
        if not credentials.exists(): credentials=Path.home()/".config/earthengine/credentials"
        available=importlib.util.find_spec("ee") is not None
        return {"schema":"kfm-ee-download-control/v1","configured":bool(project and credentials.is_file() and available),
                "project":project,"dependencyAvailable":available,"credentialsPresent":credentials.is_file(),
                "destination":str(self.raw),"sessionToken":self.token,"active":self.active,
                "authentication":self.signin.status(),"datasets":list(SPECS),"limitBytes":MAX_BYTES,"jobs":[dict(j) for j in list(self.jobs.values())[-100:]]}

    def update(self,identifier,**fields):
        with self.lock:
            self.jobs[identifier].update(fields,updatedAt=utc_now())
            save_state(self.work/"jobs"/(identifier+".json"),self.jobs[identifier])

    def start(self,value):
        if not isinstance(value,dict) or set(value)!={"selection","requestId"} or not isinstance(value["requestId"],str) or not ID.fullmatch(value["requestId"]): raise ValueError("INVALID_JOB_REQUEST")
        plan=selection(value["selection"])
        identifier=value["requestId"]
        with self.lock:
            if identifier in self.jobs:
                if self.jobs[identifier]["selection"]!=value["selection"]: raise ValueError("REQUEST_ID_CONFLICT")
                return dict(self.jobs[identifier])
            if self.active: raise ValueError("DOWNLOAD_ALREADY_RUNNING")
            if self.signin.status() in {"waiting","validating"}: raise ValueError("SIGN_IN_IN_PROGRESS")
            if len(self.jobs)>=1000: raise ValueError("JOB_HISTORY_LIMIT")
            if not self.health()["configured"]: raise ValueError("EARTH_ENGINE_SETUP_REQUIRED")
            if shutil.disk_usage(self.root).free<plan["maxBytes"]+64*1024*1024: raise ValueError("INSUFFICIENT_FREE_SPACE_FOR_LIMIT")
            parent=self.raw/plan["dataset"]/plan["period"]
            check_directory(parent,create=True)
            destination=parent/identifier
            create_candidate(destination)
            job={"id":identifier,"selection":value["selection"],"state":"queued","bytes":0,"completed":0,"total":0,
                 "destination":str(destination),"mapReady":False,"review":"UNREVIEWED","createdAt":utc_now(),"updatedAt":utc_now()}
            self.jobs[identifier]=job
            save_state(self.work/"jobs"/(identifier+".json"),job)
            self.active=identifier
            self.cancel_event.clear()
            threading.Thread(target=self.run,args=(identifier,destination),daemon=True).start()
            return dict(job)

    def run(self,identifier,destination):
        digests=[]
        request=self.jobs[identifier]["selection"]
        def write(name,body):
            if shutil.disk_usage(self.root).free<len(body)+64*1024*1024: raise ValueError("DISK_SPACE_LOW")
            write_candidate(destination,name,body)
            digest,count=hash_regular(destination/name,len(body),expected_size=len(body))
            if digest!=hashlib.sha256(body).hexdigest(): raise ValueError("STORED_BYTES_CHANGED")
            digests.append({"name":name,"sha256":digest,"bytes":count})
        try:
            self.update(identifier,state="preparing")
            import ee
            ee.data.setDeadline(90000)
            ee.Initialize(credentials=ee_credentials(self.work),project=self.configuration()["project"])
            capture(request,ee,write,lambda **kw:self.update(identifier,**kw),self.cancel_event.is_set)
        except Exception as error:
            code=str(error)
            if not re.fullmatch(r"[A-Z][A-Z0-9_]{2,90}",code): code="EARTH_ENGINE_REQUEST_FAILED"
            self.update(identifier,state="cancelled" if code=="CANCELLED" else "failed",reason=code)
        finally:
            receipt={"schema":"kfm-ee-download-receipt/v1","job":self.jobs[identifier],"files":digests,
                     "providerChecksumVerified":False,"captureIntegrity":"sha256 and stored-byte readback","admission":"NOT_ADMITTED","release":"NOT_RELEASED"}
            try: write_new(self.receipts/(identifier+".json"),json.dumps(receipt,sort_keys=True).encode())
            except Exception: self.update(identifier,state="failed",reason="RECEIPT_WRITE_FAILED")
            finally:
                with self.lock: self.active=None

    def cancel(self,identifier):
        with self.lock:
            if identifier!=self.active: raise ValueError("NO_ACTIVE_DOWNLOAD")
            self.cancel_event.set()
        return {"cancelling":identifier}

def handler(manager):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self,*args): pass
        def authorized(self):
            return self.headers.get("Host")==f"127.0.0.1:{PORT}" and self.headers.get("Origin") in ORIGINS
        def answer(self,status,body):
            encoded=json.dumps(body).encode()
            self.send_response(status)
            if self.authorized(): self.send_header("Access-Control-Allow-Origin",self.headers["Origin"])
            self.send_header("Vary","Origin")
            self.send_header("Cache-Control","no-store")
            self.send_header("Content-Type","application/json")
            self.send_header("Content-Length",str(len(encoded)))
            self.end_headers()
            self.wfile.write(encoded)
        def do_OPTIONS(self):
            if not self.authorized(): return self.answer(403,{"error":"ORIGIN_REJECTED"})
            self.send_response(204)
            self.send_header("Access-Control-Allow-Origin",self.headers["Origin"])
            self.send_header("Access-Control-Allow-Methods","GET, POST, OPTIONS")
            self.send_header("Access-Control-Allow-Headers","Content-Type, X-KFM-Session")
            self.send_header("Access-Control-Allow-Private-Network","true")
            self.send_header("Vary","Origin")
            self.end_headers()
        def do_GET(self):
            parsed=urlsplit(self.path)
            if parsed.path=="/oauth/callback" and self.headers.get("Host")==f"127.0.0.1:{PORT}":
                try:
                    with manager.lock: claimed=manager.signin.claim(parsed.query)
                except ValueError:return self.answer(403,{"error":"INVALID_OAUTH_RESPONSE"})
                if claimed:threading.Thread(target=manager.signin.finish,args=(claimed,),daemon=True).start()
                body=b"<!doctype html><title>KFM Google sign-in</title><h1>Return to KFM</h1><p>KFM is checking your Earth Engine project. The download panel will show the connection result.</p>"
                self.send_response(200);self.send_header("Content-Type","text/html; charset=utf-8");self.send_header("Content-Length",str(len(body)));self.send_header("Cache-Control","no-store");self.send_header("Referrer-Policy","no-referrer");self.send_header("Content-Security-Policy","default-src 'none'; frame-ancestors 'none'");self.end_headers();self.wfile.write(body)
                return
            if not self.authorized(): return self.answer(403,{"error":"ORIGIN_REJECTED"})
            if self.path=="/library": return self.answer(200,manager.library.snapshot(start=True))
            if self.path!="/status": return self.answer(404,{"error":"NOT_FOUND"})
            self.answer(200,manager.health())
        def do_POST(self):
            if not self.authorized() or not secrets.compare_digest(self.headers.get("X-KFM-Session",""),manager.token): return self.answer(403,{"error":"SESSION_REJECTED"})
            if self.headers.get("Content-Type")!="application/json" or self.headers.get("Transfer-Encoding"): return self.answer(415,{"error":"JSON_REQUIRED"})
            try:
                length=int(self.headers.get("Content-Length","0"))
                if not 0<length<=16384: raise ValueError("REQUEST_BYTE_LIMIT")
                self.connection.settimeout(5)
                value=json.loads(self.rfile.read(length))
                if self.path=="/auth/start":
                    with manager.lock:
                        if manager.active:raise ValueError("DOWNLOAD_ALREADY_RUNNING")
                        result=manager.signin.start(value)
                elif self.path=="/downloads": result=manager.start(value)
                elif self.path=="/library/refresh":
                    if not isinstance(value,dict) or value: raise ValueError("EMPTY_REFRESH_REQUIRED")
                    result=manager.library.refresh()
                elif self.path=="/cancel" and isinstance(value,dict) and set(value)=={"id"}: result=manager.cancel(value["id"])
                else: return self.answer(404,{"error":"NOT_FOUND"})
                self.answer(200,result)
            except (ValueError,KeyError,TypeError) as error:
                code=str(error)
                self.answer(400,{"error":code if re.fullmatch(r"[A-Z][A-Z0-9_]{2,90}",code) else "INVALID_REQUEST"})
    return Handler

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation",choices=("serve","setup","status"))
    parser.add_argument("--root",type=Path,default=Path.home()/"Projects/KFM-data")
    parser.add_argument("--project")
    args=parser.parse_args()
    os.environ["KFM_DATA_ROOT"]=str(args.root)
    validate_root(args.root)
    if args.operation=="setup":
        if not args.project or not re.fullmatch(r"[a-z][a-z0-9-]{4,61}[a-z0-9]",args.project): parser.error("Provide the registered Earth Engine project ID with --project.")
        import ee
        ee.Authenticate()
        ee.Initialize(project=args.project)
        config=args.root/"data/work/earth-engine-downloads/config.json"
        check_directory(config.parent,create=True)
        save_state(config,{"project":args.project,"configuredAt":utc_now()})
        print("Earth Engine login configured. Start the local download control.")
        return
    lock=os.open(args.root/".earth-engine-downloads.lock",os.O_CREAT|os.O_RDWR|getattr(os,"O_NOFOLLOW",0),0o600)
    fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    manager=Downloads(args.root)
    if args.operation=="status":
        health=manager.health();health.pop("sessionToken");print(json.dumps(health))
    else:
        server=ThreadingHTTPServer(("127.0.0.1",PORT),handler(manager))
        print(f"KFM Earth Engine download control: 127.0.0.1:{PORT}",flush=True)
        try: server.serve_forever()
        finally: manager.cancel_event.set();server.server_close()

if __name__=="__main__": main()
