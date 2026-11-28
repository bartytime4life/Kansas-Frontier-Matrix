"""Prepare owner-selected Qwen metadata on the runtime disk; never accept or write to the data store."""
import argparse
from contextlib import closing
import hashlib
import os
import fcntl
import json
from pathlib import Path
import signal
import sqlite3
import subprocess
import time

from tools.local_data import ai_acceptance as ai,intake,intake_review
from tools.local_data.file_io import hash_regular,read_regular
from tools.local_data.manage import utc_now
from tools.local_data.review_cache import Cache,key_for
from tools.local_data.smart_intake import Packets


def current_item(root,item_id):
    with closing(sqlite3.connect((root/'data/work/intake/index.sqlite').as_uri()+'?mode=ro',uri=True)) as db:
        job=db.execute('SELECT state,error FROM ai_acceptance_jobs ORDER BY rowid DESC LIMIT 1').fetchone()
        row=db.execute('SELECT '+','.join(intake.ITEM_COLUMNS)+' FROM items WHERE id=?',(item_id,)).fetchone()
        item=intake._row_item(row,intake.ITEM_COLUMNS);item['review_history']=intake_review.history(db,item_id)
    return item,job


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--config',required=True,type=Path)
    args=parser.parse_args();config=json.loads(args.config.read_text());runtime=args.config.parent
    identity=json.loads((runtime/'storage-identity.json').read_text());root=Path(identity['root'])
    def guard():
        if json.loads((runtime/'storage-identity.json').read_text()) != identity:
            raise RuntimeError('AI_PREPARATION_LAYOUT_CHANGED')
        subprocess.run(['/usr/bin/python3',str(runtime/'check-data-mount.py')],check=True,stdout=subprocess.DEVNULL)
    guard()
    lock=os.open(root/'data/work/intake/.qwen-review.lock',os.O_RDWR|getattr(os,'O_NOFOLLOW',0))
    fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    raw=read_regular(Path(config['owner_policy_source']),4*1024**2)
    if hashlib.sha256(raw).hexdigest()!=config['owner_policy']:raise ValueError('OWNER_POLICY_SOURCE_CHANGED')
    policy=json.loads(raw);cache=Cache(runtime.parent/'run/smart-intake-cache.sqlite')
    client=ai.Qwen(config['model'],config['model_digest']);client.identity();builder=Packets(root)
    stopping=[False]
    def stop(_sig,_frame):stopping[0]=True
    signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop)
    prepared=0;cached=0;accepted=0;changed=[];errors=[]
    for item_id,binding in policy['items'].items():
        if stopping[0]:break
        guard()
        # Read current WAL-visible rows without schema initialization or catalog writes.
        item,job=current_item(root,item_id)
        if job and job[1] in {'ADMIN_PAUSED','ADMIN_CANCELLED'}:
            stopping[0]=True;break
        if item['status']=='reviewed':accepted+=1;continue
        if item['sha256']!=binding['sha256'] or intake_review.context(item)!=binding['context']:
            changed.append(item_id);continue
        key=key_for(item,client)
        if cache.get(key):cached+=1;continue
        try:
            path=ai.source_path(root,item)
            if hash_regular(path,intake.DEFAULT_HASH_LIMIT,expected_size=item['size_bytes'])[0]!=item['sha256']:
                raise ValueError('AI_SOURCE_CHANGED_REANALYZE')
            packet=builder(root,item);review,response_hash=client.review(packet)
            cache.put(key,packet,review,client,response_hash);prepared+=1
        except (ValueError,OSError,ai.ProviderError) as error:
            errors.append({'id':item_id,'error':str(error)[:120]})
        report={'at':utc_now(),'pid':os.getpid(),'state':'paused' if stopping[0] else 'preparing','prepared':prepared,'cached':cached,
                'alreadyAccepted':accepted,'selection':len(policy['items']),'changed':changed,'errors':errors}
        (runtime.parent/'run/smart-intake-preparation.json').write_text(json.dumps(report,indent=2)+'\n')
        print(json.dumps({k:v for k,v in report.items() if k not in {'changed','errors'}}),flush=True)
    report={'at':utc_now(),'pid':os.getpid(),'state':'paused' if stopping[0] else 'prepared','prepared':prepared,'cached':cached,
            'alreadyAccepted':accepted,'selection':len(policy['items']),'changed':changed,'errors':errors}
    (runtime.parent/'run/smart-intake-preparation.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report),flush=True)
    os.close(lock)


if __name__=='__main__':main()
