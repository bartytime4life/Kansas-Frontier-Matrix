"""Recovery evidence and command plans; deliberately contains no command executor."""
from __future__ import annotations
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import sqlite3
import stat

from .accounts import AccessError
from .acceptance import canonical, decode

GATES = (
    ("device_identity", "Identify both physical drives", "Record serials, filesystem UUIDs, roles and LVM member mapping. A size or /dev name alone is not positive identity."),
    ("mount_capacity", "Verify mounts and capacity", "Confirm actual mounted devices, paths, free bytes and reserve floors. A directory on the OS drive is not the data mount."),
    ("filesystem_health", "Review drive and filesystem health", "Retain SMART reports and read-only health findings. Do not run repair on the only copy."),
    ("archive_layout", "Preserve the original archive", "Record the original layout, KFM locations, file inventory, hashes and timestamps without moving or deleting source material."),
    ("database_snapshot", "Validate databases and snapshots", "Record the consistent snapshot method, SQLite integrity/foreign-key checks on copies, and WAL/SHM/journal completeness. A copied live DB file alone is insufficient."),
    ("backup_coverage", "Establish backup coverage", "Account for originals, working data, catalogs, receipts, Studio evidence and local account recovery. Retain exclusions, backup timestamps and a separate destination."),
    ("restore_rehearsal", "Rehearse recovery on a separate copy", "Record a separately approved disposable restore, compared hashes and counts, rollback notes, and unresolved risks before operational recovery."),
)
GATE_IDS = {g[0] for g in GATES}
# Display-only examples. Device-specific placeholders must be resolved by an operator.
PLANS = (
    {"id":"identity", "title":"Device inventory", "command":"lsblk -b -o NAME,PATH,SIZE,MODEL,SERIAL,FSTYPE,UUID,MOUNTPOINTS", "scope":"Read-only Linux inventory. Do not identify a drive by size alone."},
    {"id":"mounts", "title":"Mounted sources and capacity", "command":"findmnt --real --output SOURCE,TARGET,FSTYPE,OPTIONS\ndf -B1 --output=source,target,size,used,avail", "scope":"Read-only metadata; compare every KFM path with the positively identified mount."},
    {"id":"lvm", "title":"LVM membership", "command":"sudo pvs --readonly -o pv_name,pv_uuid,vg_name,pv_size,pv_free\nsudo lvs --readonly -a -o lv_name,vg_name,lv_uuid,lv_size,segtype,devices", "scope":"Plan only. Requires operator review and permissions; no initialization or activation."},
    {"id":"smart", "title":"SMART report", "command":"sudo smartctl --all <POSITIVELY_IDENTIFIED_DEVICE>", "scope":"Plan only. Replace the placeholder after checking serial/UUID; do not start a repair or destructive test."},
    {"id":"db", "title":"Snapshot integrity", "command":"sqlite3 -readonly <VERIFIED_DISPOSABLE_SNAPSHOT> 'PRAGMA quick_check; PRAGMA foreign_key_check;'", "scope":"Plan only; use a consistent, separate snapshot, not a guessed live database. Keep WAL/SHM/journal evidence."},
)
MAX_EVENTS = 2000
MAX_TOTAL = 32 * 1024 * 1024
DEVICE_KEYS = {"label", "serial", "uuid", "filesystem", "mountpoint", "device", "lvmMembers", "totalBytes", "freeBytes", "floorBytes"}


def stamp(value):
    if not isinstance(value, str) or len(value) > 64:
        raise AccessError("OBSERVATION_TIME_REQUIRED")
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if dt.utcoffset() is None: raise ValueError()
    except ValueError as exc:
        raise AccessError("OBSERVATION_TIME_WITH_TIMEZONE_REQUIRED") from exc
    return value


def text(value, key, required=True, limit=12000):
    item = value.get(key, "")
    if not isinstance(item, str) or len(item) > limit or (required and not item.strip()):
        raise AccessError("INVALID_" + key.upper())
    return item.strip()


class RecoveryStore:
    def __init__(self, root):
        self.root = Path(root).absolute()
        self.path = self.root / "studio-recovery.sqlite3"

    @contextmanager
    def db(self, write=False):
        if self.root.is_symlink() or not self.root.is_dir() or self.root.stat().st_mode & 0o077:
            raise AccessError("PRIVATE_RECOVERY_ROOT_REQUIRED", 503)
        if self.path.is_symlink(): raise AccessError("UNSAFE_RECOVERY_STORAGE", 503)
        if not self.path.exists():
            if not write:
                yield None; return
            fd=os.open(self.path, os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW, 0o600); os.close(fd)
        for path in (self.path, Path(str(self.path)+'-journal'), Path(str(self.path)+'-wal'), Path(str(self.path)+'-shm')):
            if path.exists() or path.is_symlink():
                info=path.lstat()
                if not stat.S_ISREG(info.st_mode) or info.st_uid != os.getuid() or info.st_mode & 0o077 or info.st_nlink != 1:
                    raise AccessError("UNSAFE_RECOVERY_STORAGE", 503)
        db=sqlite3.connect(self.path.as_uri()+('?mode=rw' if write else '?mode=ro'), uri=True, timeout=5)
        db.row_factory=sqlite3.Row
        try:
            if write:
                db.execute('CREATE TABLE IF NOT EXISTS events (sequence INTEGER PRIMARY KEY, request_id TEXT UNIQUE NOT NULL, body TEXT NOT NULL, previous TEXT NOT NULL, digest TEXT NOT NULL)'); db.commit()
            db.execute('BEGIN IMMEDIATE' if write else 'BEGIN')
            yield db
            if write: db.commit()
        except BaseException:
            db.rollback(); raise
        finally: db.close()

    @staticmethod
    def _read(db):
        events=[]; previous='0'*64
        if db is not None:
            for row in db.execute('SELECT * FROM events ORDER BY sequence'):
                if row['sequence'] != len(events)+1 or row['previous'] != previous:
                    raise AccessError('RECOVERY_CHAIN_INTEGRITY_FAILURE', 503)
                value=decode(row['body'].encode())
                actual=hashlib.sha256(canonical({'sequence':row['sequence'],'previous':previous,'event':value})).hexdigest()
                if actual != row['digest']: raise AccessError('RECOVERY_CHAIN_INTEGRITY_FAILURE',503)
                events.append({'sequence':row['sequence'],'event':value,'previous':previous,'digest':actual}); previous=actual
        return events

    def snapshot(self):
        with self.db() as db: events=self._read(db)
        latest_storage=next((e for e in reversed(events) if e['event']['kind']=='storage'),None)
        revision=latest_storage['sequence'] if latest_storage else 0
        gates=[]
        for key,title,expectation in GATES:
            observation=next((e for e in reversed(events) if e['event']['kind']=='observation' and e['event']['gate']==key and e['event']['storageRevision']==revision),None)
            review=next((e for e in reversed(events) if e['event']['kind']=='review' and observation and e['event']['observation']==observation['sequence']),None)
            status='UNVERIFIED'
            if observation:
                status=observation['event']['result']
                if status=='PASS': status='AWAITING_REVIEW'
            if review:
                status='REVIEWED_EVIDENCE' if review['event']['decision']=='ACCEPT_EVIDENCE' else review['event']['decision']
            gates.append({'id':key,'title':title,'expected':expectation,'status':status,
                          'observation':observation['sequence'] if observation else None})
        return {'schema':'kfm-local-recovery-ledger/v1','storageRevision':revision,'storage':latest_storage['event']['devices'] if latest_storage else None,
                'intendedRoles':{'source':'Owner-intended 14TB main source; identity unverified','backup':'Owner-intended 1.5TB backup; identity unverified'},
                'gates':gates,'events':events,'plans':PLANS,'operationalDecision':'HOLD',
                'authority':{'executeCommands':False,'format':False,'restore':False,'changeMounts':False,'enableServices':False,'publish':False},
                'scope':'Operator-recorded evidence. Reviewed evidence is not an authorization to restore or proof of machine state.'}

    def append(self, actor, value):
        if actor['role'] not in {'operator','admin'}: raise AccessError('OPERATOR_REQUIRED',403)
        if not isinstance(value,dict): raise AccessError('EVENT_OBJECT_REQUIRED')
        kind=value.get('kind')
        common={'kind','requestId','observedAt'}
        event={'kind':kind,'actor':actor['username'],'userId':actor['id'],'observedAt':stamp(value.get('observedAt'))}
        request_id=text(value,'requestId',limit=128)
        if not re.fullmatch(r'[A-Za-z0-9_.:-]{1,128}',request_id): raise AccessError('INVALID_REQUEST_ID')
        if kind=='storage':
            if actor['role']!='admin': raise AccessError('ADMIN_REQUIRED',403)
            if set(value)-common-{'devices','notes'}: raise AccessError('UNKNOWN_STORAGE_FIELDS')
            devices=value.get('devices')
            if not isinstance(devices,dict) or set(devices)!={'source','backup'}: raise AccessError('TWO_DRIVE_ROLES_REQUIRED')
            for role,device in devices.items():
                if not isinstance(device,dict) or set(device)-DEVICE_KEYS: raise AccessError('INVALID_DEVICE_FIELDS')
                for key,item in device.items():
                    if key.endswith('Bytes'):
                        if item is not None and (type(item) is not int or not 0 <= item <= 2**63-1): raise AccessError('INVALID_CAPACITY')
                    elif not isinstance(item,str) or len(item)>2000 or '\x00' in item: raise AccessError('INVALID_DEVICE_IDENTITY')
                if device.get('freeBytes') is not None and device.get('totalBytes') is not None and device['freeBytes']>device['totalBytes']: raise AccessError('INVALID_CAPACITY')
            for key in ('serial','uuid','mountpoint'):
                if devices['source'].get(key) and devices['source'].get(key)==devices['backup'].get(key): raise AccessError('BACKUP_MUST_BE_DISTINCT_FROM_SOURCE')
            event.update(devices=devices,notes=text(value,'notes',False))
        elif kind=='observation':
            fields={'gate','storageRevision','result','steps','expected','observed','evidence','risk','retestOf'}
            if set(value)-common-fields: raise AccessError('UNKNOWN_OBSERVATION_FIELDS')
            if value.get('gate') not in GATE_IDS or value.get('result') not in {'PASS','FAIL','HOLD','UNVERIFIED'}: raise AccessError('INVALID_RECOVERY_CHECK')
            if type(value.get('storageRevision')) is not int: raise AccessError('STORAGE_REVISION_REQUIRED')
            event.update(gate=value['gate'],storageRevision=value['storageRevision'],result=value['result'])
            for key in ('steps','expected','observed','evidence','risk'): event[key]=text(value,key,key in {'steps','expected','observed'})
            if event['result']=='PASS' and not event['evidence']: raise AccessError('PASS_REQUIRES_EVIDENCE')
            reference=value.get('retestOf')
            if reference is not None and (type(reference) is not int or reference<1): raise AccessError('INVALID_RETEST_REFERENCE')
            event['retestOf']=reference
        elif kind=='review':
            if actor['role']!='admin': raise AccessError('ADMIN_REQUIRED',403)
            if set(value)-common-{'observation','decision','reason'}: raise AccessError('UNKNOWN_REVIEW_FIELDS')
            if type(value.get('observation')) is not int or value.get('decision') not in {'HOLD','RETEST','ACCEPT_EVIDENCE'}: raise AccessError('INVALID_RECOVERY_REVIEW')
            event.update(observation=value['observation'],decision=value['decision'],reason=text(value,'reason'))
        else: raise AccessError('UNKNOWN_RECOVERY_ACTION')
        with self.db(True) as db:
            events=self._read(db)
            old=db.execute('SELECT * FROM events WHERE request_id=?',(request_id,)).fetchone()
            if old:
                prior=decode(old['body'].encode()); prior.pop('recordedAt',None)
                if prior!=event: raise AccessError('REQUEST_ID_CONFLICT',409)
                return {'sequence':old['sequence'],'duplicate':True}
            latest=next((e for e in reversed(events) if e['event']['kind']=='storage'),None)
            revision=latest['sequence'] if latest else 0
            if kind=='observation':
                if not revision or event['storageRevision']!=revision: raise AccessError('STORAGE_CHANGED_RELOAD_AND_RETEST',409)
                if event['result']=='PASS':
                    for device in latest['event']['devices'].values():
                        if not all(device.get(k) for k in ('serial','uuid','filesystem','mountpoint')): raise AccessError('POSITIVE_DEVICE_IDENTITY_REQUIRED')
                    if event['gate']=='mount_capacity':
                        for device in latest['event']['devices'].values():
                            if any(device.get(k) is None for k in ('totalBytes','freeBytes','floorBytes')) or device['freeBytes']<device['floorBytes']: raise AccessError('CAPACITY_FLOOR_NOT_ESTABLISHED')
                if event['retestOf']:
                    target=next((e['event'] for e in events if e['sequence']==event['retestOf']),None)
                    if not target or target['kind']!='observation' or target['gate']!=event['gate']: raise AccessError('RETEST_SCOPE_MISMATCH')
            if kind=='review':
                target=next((e['event'] for e in events if e['sequence']==event['observation']),None)
                if not target or target['kind']!='observation': raise AccessError('OBSERVATION_REQUIRED')
                if event['decision']=='ACCEPT_EVIDENCE':
                    if target['result']!='PASS' or target['storageRevision']!=revision: raise AccessError('CURRENT_PASS_EVIDENCE_REQUIRED',409)
                    newest=next(e for e in reversed(events) if e['event']['kind']=='observation' and e['event']['gate']==target['gate'] and e['event']['storageRevision']==revision)
                    if newest['sequence']!=event['observation']: raise AccessError('SUPERSEDED_OBSERVATION',409)
            if len(events)>=MAX_EVENTS: raise AccessError('RECOVERY_LEDGER_FULL',503)
            event['recordedAt']=datetime.now(timezone.utc).isoformat()
            body=canonical(event)
            used=db.execute('SELECT COALESCE(SUM(length(CAST(body AS BLOB))),0) FROM events').fetchone()[0]
            if used+len(body)>MAX_TOTAL: raise AccessError('RECOVERY_LEDGER_FULL',503)
            seq=len(events)+1; previous=events[-1]['digest'] if events else '0'*64
            digest=hashlib.sha256(canonical({'sequence':seq,'previous':previous,'event':event})).hexdigest()
            db.execute('INSERT INTO events VALUES (?,?,?,?,?)',(seq,request_id,body.decode(),previous,digest))
        return {'sequence':seq,'operationalDecision':'HOLD'}

    def export(self):
        payload=self.snapshot()
        return canonical({'algorithm':'SHA-256','digest':hashlib.sha256(canonical(payload)).hexdigest(),
                          'scope':'Local recovery evidence only; no account secrets, operational command execution or authorization.', 'payload':payload})
