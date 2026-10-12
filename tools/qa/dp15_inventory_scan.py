#!/usr/bin/env python3
"""Read-only, commit-pinned lexical DP inventory. No code from the target runs."""
import argparse, collections, csv, gzip, hashlib, io, json, pathlib, re, struct, subprocess, tarfile

QUERIES = {
    'dp_explicit': r'differential[ _-]*privacy|differentially[ _-]*private|DPBudget\w*|DPReceipt\w*|privacy[ _-]*(?:budget|loss|account\w*|ledger)|dp[ _-]*(?:budget|receipt|ledger|account\w*|mechanism|aggregate\w*|noise\w*|noised|variant|release|profile)',
    'dp_alias': r'\b(?:DP|RDP|zCDP|CDP|LDP|GDP|DAS|TopDown)\b|\b(?:DP[0-9]{2}|DP[_-]\w+|GDP[_-]\w+|CDP[_-]\w+)|disclosure[ _-]*avoidance|privacy[ _-]*preserv\w*|privati[sz]\w*|r[ée]nyi|zero[ -]concentrated|approximate[ _-]*dp|pure[ _-]*dp|local[ _-]*dp|dp[-_ ]?sgd',
    'dp_library': r'google[ _-]*dp|\b(?:opendp|diffprivlib|opacus|pydp|pipeline[-_]?dp|smartnoise|snsql|snsynthetic|dp[-_]accounting|tensorflow[-_]privacy|privacy[-_]on[-_]beam|tmlt|tumult|chorus|differential[-_]privacy)\b',
    'mechanism': r'\b(?:epsilon|eps|laplace|laplacian|gaussian|normalvariate|privacy_spent|compute_epsilon|noise_scale|add_noise|accountant\w*|odometer\w*|randomi[sz]ed[ _-]*response|exponential[ _-]*mechanism|geometric[ _-]*mechanism|private[ _-]*histogram|private[ _-]*count\w*|privacy[ _-]*filter|neighboring[ _-]*(?:dataset|relation)|contribution[ _-]*bound\w*)\b|[εδ]',
    'broad_support': r'\b(?:noise\w*|nois[ey]\w*|clipp?ing|clipped|clip|budget\w*|ledger\w*|sensitivity|delta|composition|anonym\w*|privaci\w*|privacy|private)\b',
}
RX = {k: re.compile(v, re.I) for k,v in QUERIES.items()}

def run(*args): return subprocess.check_output(args)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('repo'); ap.add_argument('ref'); ap.add_argument('out'); a=ap.parse_args()
    repo=pathlib.Path(a.repo).resolve(); out=pathlib.Path(a.out).resolve(); out.mkdir(parents=True,exist_ok=True)
    def git(*args): return run('git','-C',str(repo),*args)
    commit=git('rev-parse',a.ref+'^{commit}').decode().strip(); tree=git('rev-parse',commit+'^{tree}').decode().strip()
    rawtree=git('ls-tree','-r','-z','--full-tree',commit)
    entries=[]; hits=[]; decoded=[]; errors=[]; binaries=[]
    proc=subprocess.Popen(['git','-C',str(repo),'cat-file','--batch'],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
    def scan(path, text, sha, kind):
        for number,line in enumerate(text.splitlines(),1):
            matched={k: sorted(set(m.group(0) for m in rx.finditer(line)),key=lambda term: (term.casefold(), term)) for k,rx in RX.items() if rx.search(line)}
            if matched: hits.append(dict(path=path,line=number,blob=sha,representation=kind,queries=matched,text=line))
        matched={k: sorted(set(m.group(0) for m in rx.finditer(path)),key=lambda term: (term.casefold(), term)) for k,rx in RX.items() if rx.search(path)}
        if matched: hits.append(dict(path=path,line=0,blob=sha,representation='path',queries=matched,text=path))
    def decode(path, data, sha, kind):
        try:
            text=data.decode('utf-8')
            if '\x00' in text: raise ValueError('NUL bytes')
            decoded.append(dict(path=path,representation=kind,bytes=len(data),sha256=hashlib.sha256(data).hexdigest()))
            scan(path,text,sha,kind); return True
        except (UnicodeDecodeError, ValueError): return False
    for entry in rawtree.split(b'\0'):
        if not entry: continue
        meta,path=entry.split(b'\t',1); mode,typ,sha=meta.decode().split(); path=path.decode()
        if typ!='blob': errors.append(dict(path=path,error='non-blob:'+typ)); continue
        proc.stdin.write((sha+'\n').encode()); proc.stdin.flush(); header=proc.stdout.readline().decode().split(); data=proc.stdout.read(int(header[2])); assert proc.stdout.read(1)==b'\n'
        assert hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==sha
        entries.append(dict(path=path,mode=mode,blob=sha,bytes=len(data),sha256=hashlib.sha256(data).hexdigest()))
        if path.endswith(('.tgz','.tar.gz')):
            try:
                with tarfile.open(fileobj=io.BytesIO(data),mode='r:gz') as tar:
                    for member in tar.getmembers():
                        memberpath=path+'::'+member.name
                        if member.isfile():
                            memberdata=tar.extractfile(member).read()
                            if not decode(memberpath,memberdata,sha,'tar-member'):
                                binaries.append(dict(path=memberpath,container=path,bytes=len(memberdata),kind='binary-tar-member'))
            except Exception as e: errors.append(dict(path=path,error=str(e)))
        elif path.endswith('.gz'):
            try:
                if not decode(path+'::gunzip',gzip.decompress(data),sha,'gzip-text'): errors.append(dict(path=path,error='nontext gzip'))
            except Exception as e: errors.append(dict(path=path,error=str(e)))
        elif data.startswith(b'%PDF'):
            try:
                p=subprocess.run(['pdftotext','-layout','-','-'],input=data,capture_output=True,check=True)
                decode(path+'::pdftotext',p.stdout,sha,'pdf-text')
            except Exception as e: errors.append(dict(path=path,error=str(e)))
        elif data.startswith(b'glTF'):
            offset=12
            while offset<len(data):
                size,ct=struct.unpack_from('<II',data,offset); chunk=data[offset+8:offset+8+size]; offset+=8+size
                if ct==0x4e4f534a: decode(path+'::JSON',chunk,sha,'glb-json')
            binaries.append(dict(path=path,bytes=len(data),kind='glb-geometry'))
        elif decode(path,data,sha,'utf8'): pass
        else:
            # Scan printable metadata, not random binary bytes as UTF-8 text.
            strings=b'\n'.join(re.findall(rb'[\x20-\x7e]{6,}',data))
            decode(path+'::strings',strings,sha,'binary-strings')
            kind=subprocess.run(['file','-b','-'],input=data,capture_output=True,check=True).stdout.decode().strip()
            binaries.append(dict(path=path,bytes=len(data),kind=kind))
    proc.stdin.close(); proc.wait(); assert proc.returncode==0
    roots=collections.Counter(p['path'].split('/')[0] for p in entries)
    summary=dict(commit=commit,tree=tree,tree_manifest_sha256=hashlib.sha256(rawtree).hexdigest(),tracked_blobs=len(entries),total_bytes=sum(e['bytes'] for e in entries),modes=dict(collections.Counter(e['mode'] for e in entries)),roots=dict(sorted(roots.items())),queries=QUERIES,decoded_representations=len(decoded),binary_assets=binaries,errors=errors,hit_lines=len(hits),hit_paths=len(set(h['path'] for h in hits)),query_counts={k:dict(lines=sum(k in h['queries'] for h in hits),paths=len(set(h['path'] for h in hits if k in h['queries']))) for k in RX},tools=dict(python=run('python','--version').decode().strip(),git=git('--version').decode().strip(),pdftotext=subprocess.run(['pdftotext','-v'],capture_output=True).stderr.decode().splitlines()[0]))
    for name,value in [('summary',summary),('tree-manifest',entries),('decoded-manifest',decoded),('hits',hits)]:
        (out/(name+'.json')).write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({k:v for k,v in summary.items() if k not in ('queries','roots','binary_assets')},indent=2))

if __name__=='__main__': main()
