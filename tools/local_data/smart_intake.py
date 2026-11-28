"""Resumable local Qwen intake, exact owner exceptions, and a single metadata catalog."""
import argparse
from contextlib import closing
import csv
import gzip
import hashlib
import io
import json
import os
from pathlib import Path
import signal
import sqlite3
import subprocess
import time

from tools.local_data import ai_acceptance as ai, intake, intake_review, intake_route
from tools.local_data.file_io import read_regular, write_new
from tools.local_data.manage import canonical, utc_now

ADMIN = 'KFM owner (scheduled local Qwen review)'
BACKUP_UNITS = ('kfm-initial-backup.service','kfm-files-backup.service',
    'kfm-bulk-snapshot.service','kfm-sql-snapshot.service')
PROVIDERS = {
    'asos-5min': ('atmosphere', 'ASOS station observation archive'),
    'census-acs': ('settlements-infrastructure', 'Census ACS tabular capture'),
    'fema': ('hazards', 'FEMA mitigation program records'),
    'gbif': ('', 'GBIF occurrence capture; taxonomy and sensitive locations require content review'),
    'ghcnd': ('atmosphere', 'GHCN daily station records'),
    'iem-wind': ('atmosphere', 'IEM wind observation capture'),
    'newspaper-text': ('', 'Newspaper catalog or OCR capture'),
    'nwm': ('hydrology', 'National Water Model output capture'),
    'usgs-daily': ('hydrology', 'USGS daily water observations'),
    'usgs-groundwater': ('hydrology', 'USGS groundwater measurements'),
    'usgs-streamflow': ('hydrology', 'USGS streamflow capture'),
    'usgs-earthquakes': ('hazards', 'USGS earthquake capture'),
    'nws-alerts': ('hazards', 'NWS alert capture'),
    'archive-texts': ('', 'Archive catalog record and OCR text; historical statements are unverified'),
}


def emit(**data):
    print(json.dumps({'at': utc_now(), **data}), flush=True)


def operator_stopped(job):
    return bool(job and job['state'] in {'paused','cancelled'} and job.get('error') in {'ADMIN_PAUSED','ADMIN_CANCELLED'})


def backup_running(units):
    states = [value for value in subprocess.check_output(['/usr/bin/systemctl','--user','show',*units,
        '-p','ActiveState','--value'],text=True).splitlines() if value]
    if len(states)!=len(units):raise ai.ProviderError('AI_BACKUP_STATE_UNAVAILABLE')
    return any(state not in {'inactive','failed'} for state in states)


def provider(item):
    parts = Path(item['relative_path']).parts
    return parts[1] if len(parts) > 1 and parts[0] == 'sql-feeds' else parts[0]


class Packets:
    def __init__(self, root):
        self.root = root
        self.records = {}
        # Local provider metadata only. No model-generated provenance or network fetches.
        for path in sorted((root / 'data/raw/sql-feeds/archive-texts/items').glob('*.gz')):
            raw = read_regular(path, 32 * 1024**2)
            digest = hashlib.sha256(raw).hexdigest()
            total = 0
            with gzip.GzipFile(fileobj=io.BytesIO(raw)) as stream:
                while line := stream.readline(1024 * 1024 + 1):
                    total += len(line)
                    if len(line) > 1024 * 1024 or total > 256 * 1024**2:
                        raise ValueError('PROVIDER_METADATA_LIMIT_EXCEEDED')
                    value = json.loads(line)
                    if isinstance(value, dict) and value.get('identifier'):
                        record = {}
                        for k in ('identifier','title','creator','date','year','language','subject'):
                            field = value.get(k)
                            if isinstance(field,str):record[k] = field[:400]
                            elif isinstance(field,list):record[k] = [str(v)[:120] for v in field[:6]]
                        self.records[value['identifier']] = {'record': record,
                            'metadata_path': str(path.relative_to(root)), 'metadata_sha256': digest,
                            'scope': 'Bounded saved provider catalog fields; source text and identities are not independently verified.'}

    def __call__(self, root, item):
        packet = ai.packet_for(root, item)
        name = provider(item)
        if name in PROVIDERS:
            domain, label = PROVIDERS[name]
            packet['facts'].append({'id':'provider_context','text':json.dumps({
                'provider_hint':name, 'collection_hint':label, 'suggested_domain':domain,
                'limits':'Collection identity is a path hint; confirm against the inspected content. No rights grant inferred.'})})
        parts = Path(item['relative_path']).parts
        if len(parts) > 4 and parts[:3] == ('sql-feeds','archive-texts','texts'):
            record = self.records.get(parts[4])
            if record:
                packet['facts'].append({'id':'source_metadata','text':json.dumps(record,ensure_ascii=False)})
        return packet


class SmartManager(ai.Manager):
    def __init__(self, root, client, *, owner_policy=None, preparation_status=None, maintenance_file=None, backup_units=(), **kwargs):
        self.owner_policy = owner_policy
        self.preparation_status=Path(preparation_status) if preparation_status else None
        self.maintenance_file=Path(maintenance_file) if maintenance_file else None
        self.backup_units=backup_units
        original_guard=kwargs.get('check_volume',lambda:None)
        def guard():
            original_guard()
            reason=self.maintenance_reason()
            if reason:
                raise ai.ProviderError('AI_BACKUP_RUNNING' if reason=='backup' else 'AI_DATA_MAINTENANCE')
        kwargs['check_volume']=guard
        super().__init__(root, client, **kwargs)

    def maintenance_reason(self):
        if self.maintenance_file and self.maintenance_file.exists() and json.loads(self.maintenance_file.read_text()).get('phase')!='complete':
            return 'drive maintenance'
        if self.backup_units:
            try:
                if backup_running(self.backup_units):return 'backup'
            except (OSError,subprocess.SubprocessError):
                raise ai.ProviderError('AI_BACKUP_STATE_UNAVAILABLE') from None
        return None

    def status(self):
        result=super().status()
        if self.preparation_status and self.preparation_status.exists():
            result['preparation']=json.loads(self.preparation_status.read_text())
        result['maintenanceReason']=self.maintenance_reason()
        result['maintenance']=bool(result['maintenanceReason'])
        return result

    def process(self, job, task):
        result = super().process(job, task)
        item = intake.get_item(self.root, task[2])
        recovered = (item['decision'].get('operator_review') or {}).get('ai_attribution', {})
        recovered_owner = (recovered.get('acceptance_basis') == 'owner_requested_private_reference'
            and recovered.get('batch_id') == job['id'] and item['sha256'] == task[3])
        if result.get('ai_reviewed') and result['outcome'] == 'held' and self.owner_policy:
            try:
                authorization = intake_review.owner_reference_authorization(self.root, self.owner_policy, item)
            except ValueError:
                authorization = None
            extraction = result.get('attribution', {}).get('text_extraction', {})
            bad_stream = set(extraction.get('issues', ())) & {'GZIP_INVALID_OR_TRUNCATED','GZIP_TEXT_NOT_PLAINTEXT_UTF8'}
            if recovered_owner:
                operator = item['decision']['operator_review']
                result = {**result,'outcome':'accepted','attribution':recovered,
                    'source_hold_reasons':result['holds'],'holds':[],
                    'acceptance_basis':'owner_requested_private_reference',
                    'review_receipt':operator['receipt'],'reviewed_at':operator['reviewed_at']}
            elif authorization and not bad_stream and not item['decision'].get('blocking_issues'):
                self.check_volume()
                attribution = {**result['attribution'], 'acceptance_basis':'owner_requested_private_reference',
                    'owner_reference_authorization':authorization,
                    'qwen_original_recommendation':result['recommendation'],
                    'limitations_retained':list(result['holds'])}
                declared = item.get('declared') or {}
                value = {'id':item['id'],'sha256':item['sha256'],
                    'revision':item['review_history'][0]['revision'] if item['review_history'] else 0,
                    'decision':'local','domain':result['domain'] if result['domain'] != 'unassigned' else '',
                    'rights':(declared.get('rights') or {}).get('redistribution','unknown'),
                    'sensitivity':declared.get('sensitivity','unknown'),'reference':'',
                    'reviewer':'Local AI: '+self.client.model,'confirmed':True,
                    'note':('Owner requested private reference retention of this exact file. Qwen supplied the description and evidence; '
                        'its original recommendation and uncertainty remain recorded. This accepts a catalog reference, '
                        'not verified historical assertions, identities, measurements or sharing rights. '
                        +result['description'])[:1600]}
                saved = intake_review.save(self.root,value,intake_route.load_budget(),ai_attribution=attribution,
                    expected_context=task[4],owner_policy=self.owner_policy)
                result = {**result,'outcome':'accepted','attribution':attribution,
                    'source_hold_reasons':result['holds'],'holds':[],
                    'acceptance_basis':'owner_requested_private_reference',
                    'review_receipt':saved['review']['receipt'],'reviewed_at':saved['review']['reviewed_at']}
            if result['outcome'] == 'accepted':
                relative = f"data/receipts/intake/{item['id']}/owner-{job['id']}-{task[1]}.json"
                body = canonical({k:v for k,v in result.items() if k != 'receipt'})
                if (self.root / relative).exists():
                    if read_regular(self.root / relative,128*1024) != body:
                        raise ValueError('OWNER_RESOLUTION_RECEIPT_CHANGED')
                else:
                    write_new(self.root / relative,body)
                result['receipt'] = relative
        if result.get('ai_reviewed'):
            try:
                self.organize(item, result)
            except (OSError,sqlite3.Error,ValueError) as error:
                raise ai.ProviderError('AI_METADATA_CATALOG_BUSY_RESUME') from error
        emit(item=task[2],outcome=result['outcome'],basis=result.get('acceptance_basis','native_qwen_gates'))
        return result

    def organize(self, item, result):
        self.check_volume()
        folder = self.root / 'data/work/intake/smart-catalog'
        folder.mkdir(mode=0o700,parents=True,exist_ok=True)
        record = {'id':item['id'],'sha256':item['sha256'],'original':item['store_path'],
            'provider':provider(item),'domain':result['domain'],'title':result['title'],
            'description':result['description'],'outcome':result['outcome'],
            'metadata_quality':'bounded AI-assisted catalog reference; inspect the original before analytical use',
            'ai_attribution':result['attribution'],'evidence':result['evidence'],
            'review_receipt':result.get('review_receipt'),'source_hold_reasons':result.get('source_hold_reasons',result['holds']),
            'authority':{'publication':False,'source_admission':False,'release':False}}
        path = folder / 'records' / item['id'] / (result['attribution']['response_sha256'] + '.json')
        body = canonical(record)
        if path.exists():
            if read_regular(path,128*1024) != body:
                raise ValueError('SMART_METADATA_RECEIPT_CHANGED')
        else:
            write_new(path,body)
        with closing(sqlite3.connect(folder / 'catalog.sqlite',timeout=10)) as db:
            with db:
                db.execute('CREATE TABLE IF NOT EXISTS catalog(id TEXT PRIMARY KEY,sha256 TEXT,provider TEXT,domain TEXT,outcome TEXT,record TEXT)')
                db.execute('INSERT OR REPLACE INTO catalog VALUES(?,?,?,?,?,?)',
                    (item['id'],item['sha256'],provider(item),result['domain'],result['outcome'],json.dumps(record)))


def export_catalog(root):
    folder = root / 'data/work/intake/smart-catalog'
    if not (folder / 'catalog.sqlite').exists():
        return
    with closing(sqlite3.connect(folder / 'catalog.sqlite')) as db:
        rows = [json.loads(r[0]) for r in db.execute('SELECT record FROM catalog ORDER BY domain,provider,id')]
    partial = folder / '.CATALOG.csv.partial'
    fields = ['id','sha256','provider','domain','outcome','title','description','original','review_receipt']
    with partial.open('w',newline='') as f:
        writer = csv.DictWriter(f,fieldnames=fields,extrasaction='ignore')
        writer.writeheader();writer.writerows(rows)
        f.flush();os.fsync(f.fileno())
    partial.replace(folder / 'CATALOG.csv')
    # Domain manifests reference originals instead of making another set of copies.
    for domain in sorted({r['domain'] for r in rows}):
        destination = folder / 'by-domain' / (domain if domain != 'unassigned' else 'cross-domain-reference')
        destination.mkdir(parents=True,exist_ok=True,mode=0o700)
        temp = destination / '.INDEX.csv.partial'
        with temp.open('w',newline='') as f:
            writer = csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');writer.writeheader()
            writer.writerows(r for r in rows if r['domain']==domain)
            f.flush();os.fsync(f.fileno())
        temp.replace(destination / 'INDEX.csv')
    (folder / 'README.txt').write_text('KFM smart catalog\n\nCATALOG.csv and catalog.sqlite index AI-reviewed references.\n'
        'by-domain/ organizes references without duplicating original bytes.\nrecords/ contains exact descriptions, '
        'evidence, model fingerprints and acceptance receipts.\nOriginal files and earlier reviews remain in the native store.\n'
        'Private acceptance does not certify historical facts, personal identities, data quality or public-use rights.\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config',type=Path,required=True)
    args = parser.parse_args()
    os.umask(0o077)
    config = json.loads(args.config.read_text())
    runtime = args.config.parent
    state = json.loads((runtime / 'storage-identity.json').read_text())
    root = Path(state['root'])
    def guard():
        current = json.loads((runtime / 'storage-identity.json').read_text())
        if current != state or not root.is_dir():
            raise RuntimeError('AI_DATA_LAYOUT_CHANGED')
        subprocess.run(['/usr/bin/python3',str(runtime / 'check-data-mount.py')],check=True,
            stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    drive_work = Path(config.get('maintenance_directory',runtime/'maintenance'))
    def maintenance():
        phase = drive_work / 'phase.json'
        if phase.exists() and json.loads(phase.read_text()).get('phase') != 'complete':
            return 'backup verification window'
        phase = drive_work / 'consolidation-phase.json'
        if phase.exists():
            step = json.loads(phase.read_text()).get('phase')
            allowed = {'verifying-all-old-data-on-14tb','consolidation-complete'}
            if step == 'deduplicating-old-data-with-sha256':
                proof = drive_work / 'primary-layout-complete.json'
                if proof.exists() and json.loads(proof.read_text()).get('primaryRoot') == str(root.parent):
                    allowed.add(step)
            if step not in allowed:
                return 'drive layout maintenance'
        for unit in ['kfm-initial-backup.service','kfm-files-backup.service','kfm-bulk-snapshot.service','kfm-sql-snapshot.service','kfm-intake-analyze.service']:
            if subprocess.check_output(['systemctl','--user','show',unit,'-p','ActiveState','--value'],text=True).strip() in {'active','activating','deactivating'}:
                return 'catalog analysis running' if unit == 'kfm-intake-analyze.service' else 'backup running'
        return None
    if reason := maintenance():
        emit(state='deferred',reason=reason);return
    guard()
    # A compact covering index keeps live totals/groups off the large profile
    # pages while background verification is reading the same physical drive.
    with intake.writer_lock(root), intake.open_index(root) as db:
        db.execute('CREATE INDEX IF NOT EXISTS items_summary ON items(present,status,domain,family,lane,size_bytes)')
    policy_hash = config.get('owner_policy')
    if policy_hash:
        raw = read_regular(Path(config['owner_policy_source']),4*1024**2)
        if hashlib.sha256(raw).hexdigest() != policy_hash:
            raise ValueError('OWNER_POLICY_SOURCE_CHANGED')
        target = root / 'data/work/intake/owner-policies' / (policy_hash + '.json')
        if not target.exists():write_new(target,raw)
    from tools.local_data.review_cache import Cache,CachedQwen,CachedPackets
    cache=Cache(config.get('preparation_cache',runtime.parent/'run/smart-intake-cache.sqlite'))
    client = CachedQwen(config['model'],config['model_digest'],cache);client.identity()
    manager = SmartManager(root,client,check_volume=guard,packet_builder=CachedPackets(Packets(root),client,cache),owner_policy=policy_hash,
        maintenance_file=drive_work/'phase.json',preparation_status=config.get('preparation_status'),backup_units=BACKUP_UNITS)
    def pause(_signal,_frame):manager.action='pause';manager.stop.set()
    signal.signal(signal.SIGTERM,pause);signal.signal(signal.SIGINT,pause)
    current = manager.status()['job']
    if operator_stopped(current):
        emit(state='deferred',reason='paused or stopped by the admin; use Studio to resume or start a new batch',job=current['id']);return
    if current and current['state'] == 'paused':
        if current['admin'] != ADMIN:
            emit(state='deferred',reason='manual batch is paused',job=current['id']);return
        try:manager.control('resume')
        except ValueError as error:
            if str(error)=='AI_BATCH_ALREADY_RUNNING':emit(state='deferred',reason='metadata preparation owns the Qwen lock');return
            raise
    elif current and current['state'] in ai.ACTIVE:
        emit(state='deferred',reason='another Qwen batch owns the review lock');return
    else:
        try:
            manager.start({'admin':ADMIN,'filters':{},'limit':config.get('batch_limit',100),'retryHeld':False})
        except ValueError as error:
            if str(error)=='AI_BATCH_ALREADY_RUNNING':emit(state='deferred',reason='metadata preparation owns the Qwen lock');return
            if str(error)=='AI_NO_NEW_PENDING_FILES_MATCH_FILTERS':
                export_catalog(root);emit(state='idle',reason=str(error));return
            raise
    began = time.monotonic()
    for cycle in range(config.get('max_batches',1)):
        while manager.thread and manager.thread.is_alive():
            manager.thread.join(2)
            if maintenance() or time.monotonic()-began > config.get('max_run_seconds',7200):
                manager.action='pause';manager.stop.set()
        export_catalog(root)
        status = manager.status()['job']
        report = {k:status[k] for k in ('id','state','counts','currentStatuses','total','model','digest','error')}
        (runtime.parent / 'run/smart-intake-latest.json').write_text(json.dumps(report,indent=2)+'\n')
        emit(**report)
        if status['state'] != 'completed' or manager.stop.is_set() or cycle+1 >= config.get('max_batches',1) or maintenance():
            break
        try:
            manager.start({'admin':ADMIN,'filters':{},'limit':config.get('batch_limit',100),'retryHeld':False})
        except ValueError as error:
            if str(error)=='AI_NO_NEW_PENDING_FILES_MATCH_FILTERS':break
            raise


if __name__ == '__main__':
    main()
