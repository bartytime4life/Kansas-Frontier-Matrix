#!/usr/bin/env python3
"""Build or verify deterministic 3D Tiles tree hash manifests without network.

A PASS proves bounded local byte inventory and deterministic hashing only. It
is not full 3D Tiles conformance, evidence, policy, attestation, promotion,
release, publication, or public-use authority.
"""
from __future__ import annotations
import argparse, hashlib, json, math, os, stat, sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Iterable, Mapping, Sequence
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[4]
HASH_SRC = ROOT / 'packages/hashing/src'
if str(HASH_SRC) not in sys.path: sys.path.insert(0, str(HASH_SRC))
from hashing import compute_spec_hash  # noqa: E402

SCHEMA = ROOT/'schemas/contracts/v1/map/tiles3d_tree_hash_manifest.schema.json'
FIXTURES = ROOT/'fixtures/map/tiles3d_tree_hash_manifest'
CASE_MANIFEST = FIXTURES/'expected_findings_manifest.json'
MAX_FILES=1024; MAX_FILE_BYTES=64*1024*1024; MAX_TOTAL_BYTES=256*1024*1024; MAX_JSON_BYTES=4*1024*1024
SCOPE='tiles3d-tree-byte-integrity-only'
MEDIA={'.json':'application/json','.subtree':'application/octet-stream','.glb':'model/gltf-binary','.b3dm':'application/vnd.3dtiles-batched-model','.pnts':'application/vnd.3dtiles-point-cloud','.cmpt':'application/vnd.3dtiles-composite'}
class DuplicateKeyError(ValueError): pass
class NonFiniteNumberError(ValueError): pass
@dataclass(frozen=True, order=True)
class Finding: code:str; field:str
@dataclass(frozen=True)
class Result:
    manifest: dict[str,Any] | None
    findings: tuple[Finding,...]
    @property
    def ok(self)->bool: return self.manifest is not None and not self.findings
    @property
    def outcome(self)->str: return 'PASS' if self.ok else 'ERROR'

def _unique(pairs:list[tuple[str,Any]])->dict[str,Any]:
    out={}
    for k,v in pairs:
        if k in out: raise DuplicateKeyError(k)
        out[k]=v
    return out

def _reject(_v:str)->None: raise NonFiniteNumberError

def _finite(v:str)->float:
    x=float(v)
    if not math.isfinite(x): raise NonFiniteNumberError
    return x

def _load_json(path:Path)->tuple[dict[str,Any]|None,list[Finding]]:
    try:
        if path.is_symlink(): return None,[Finding('INPUT_SYMLINK_DENIED','/')]
        if not path.is_file(): return None,[Finding('INPUT_NOT_FILE','/')]
        if path.stat().st_size>MAX_JSON_BYTES: return None,[Finding('INPUT_TOO_LARGE','/')]
        value=json.loads(path.read_text(encoding='utf-8'),object_pairs_hook=_unique,parse_constant=_reject,parse_float=_finite)
    except UnicodeDecodeError: return None,[Finding('JSON_INVALID','/')]
    except DuplicateKeyError: return None,[Finding('JSON_DUPLICATE_KEY','/')]
    except NonFiniteNumberError: return None,[Finding('JSON_NONFINITE_NUMBER','/')]
    except json.JSONDecodeError: return None,[Finding('JSON_INVALID','/')]
    except OSError: return None,[Finding('INPUT_READ_ERROR','/')]
    if not isinstance(value,dict): return None,[Finding('ROOT_NOT_OBJECT','/')]
    return value,[]

def _schema_findings(value:Mapping[str,Any])->list[Finding]:
    try:
        schema=json.loads(SCHEMA.read_text(encoding='utf-8')); Draft202012Validator.check_schema(schema)
        errors=list(Draft202012Validator(schema,format_checker=FormatChecker()).iter_errors(value))
    except (OSError,UnicodeError,json.JSONDecodeError,ValueError,RecursionError): return [Finding('SCHEMA_UNAVAILABLE','/')]
    return [Finding('SCHEMA_INVALID','/'+ '/'.join(str(x) for x in e.absolute_path)) for e in errors]

def _sha(path:Path)->str:
    h=hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda:stream.read(1024*1024),b''): h.update(block)
    return 'sha256:'+h.hexdigest()

def _safe_root(path:Path)->tuple[Path|None,list[Finding]]:
    try:
        if path.is_symlink(): return None,[Finding('TREE_ROOT_SYMLINK_DENIED','/')]
        resolved=path.resolve(strict=True)
        if not resolved.is_dir(): return None,[Finding('TREE_ROOT_NOT_DIRECTORY','/')]
    except OSError: return None,[Finding('TREE_ROOT_UNAVAILABLE','/')]
    return resolved,[]

def _walk(root:Path)->tuple[list[dict[str,Any]]|None,list[Finding]]:
    findings=[]; entries=[]; total=0
    try: candidates=sorted(root.rglob('*'),key=lambda p:p.relative_to(root).as_posix())
    except OSError: return None,[Finding('TREE_WALK_ERROR','/')]
    for p in candidates:
        rel=p.relative_to(root).as_posix()
        try:
            if p.is_symlink(): findings.append(Finding('TREE_SYMLINK_DENIED','/'+rel)); continue
            mode=p.stat().st_mode
            if stat.S_ISDIR(mode): continue
            if not stat.S_ISREG(mode): findings.append(Finding('TREE_SPECIAL_FILE_DENIED','/'+rel)); continue
            size=p.stat().st_size
        except OSError: findings.append(Finding('TREE_FILE_UNREADABLE','/'+rel)); continue
        if size>MAX_FILE_BYTES: findings.append(Finding('TREE_FILE_TOO_LARGE','/'+rel)); continue
        total+=size
        if total>MAX_TOTAL_BYTES: findings.append(Finding('TREE_TOTAL_TOO_LARGE','/')); break
        suffix=p.suffix.lower(); role='tileset' if rel=='tileset.json' else ('subtree' if suffix=='.subtree' else 'content')
        entries.append({'path':rel,'byte_size':size,'sha256':_sha(p),'media_type':MEDIA.get(suffix,'application/octet-stream'),'role':role})
        if len(entries)>MAX_FILES: findings.append(Finding('TREE_FILE_COUNT_EXCEEDED','/')); break
    return (entries if not findings else None),findings

def build(tree:Path)->Result:
    root,findings=_safe_root(tree)
    if root is None: return Result(None,tuple(sorted(set(findings))))
    tileset=root/'tileset.json'
    if not tileset.is_file() or tileset.is_symlink(): return Result(None,(Finding('TILESET_MISSING','/tileset.json'),))
    tileset_obj,read_findings=_load_json(tileset)
    if tileset_obj is None: return Result(None,tuple(sorted(set(read_findings+[Finding('TILESET_INVALID','/tileset.json')]))))
    asset=tileset_obj.get('asset')
    if not isinstance(asset,dict) or not isinstance(asset.get('version'),str) or not asset['version']:
        return Result(None,(Finding('TILESET_ASSET_VERSION_MISSING','/tileset.json/asset/version'),))
    entries,walk_findings=_walk(root)
    if entries is None: return Result(None,tuple(sorted(set(walk_findings))))
    tree_hash=compute_spec_hash(entries)
    value={'object_type':'Tiles3DTreeHashManifest','schema_version':'1.0.0','manifest_id':'kfm://map/tiles3d-tree/'+tree_hash.split(':',1)[1],'status':'CANDIDATE_INTEGRITY_ONLY','canonicalization_profile':'RFC8785-JCS','digest_algorithm':'sha256','tileset_path':'tileset.json','file_count':len(entries),'total_bytes':sum(e['byte_size'] for e in entries),'tree_hash':tree_hash,'files':entries,'spec_hash':'sha256:'+'0'*64,'governance':{'source_activated':False,'evidence_resolved':False,'policy_evaluated':False,'promotion_authorized':False,'release_authorized':False,'publication_authorized':False,'tile_artifact_manifest_ref':None,'release_manifest_ref':None}}
    value['spec_hash']=compute_spec_hash({k:v for k,v in value.items() if k!='spec_hash'})
    sf=_schema_findings(value)
    return Result(value,tuple(sorted(set(sf)))) if sf else Result(value,())

def verify(tree:Path,manifest_path:Path)->Result:
    expected,findings=_load_json(manifest_path)
    if expected is None: return Result(None,tuple(sorted(set(findings))))
    sf=_schema_findings(expected)
    if sf: return Result(None,tuple(sorted(set(sf))))
    built=build(tree)
    if not built.ok: return built
    if built.manifest!=expected: return Result(None,(Finding('MANIFEST_MISMATCH','/'),))
    return built

def run_fixtures()->int:
    try: cases=json.loads(CASE_MANIFEST.read_text(encoding='utf-8'))['cases']
    except (OSError,UnicodeError,json.JSONDecodeError,KeyError): return 1
    passed=True
    for case in cases:
        tree=FIXTURES/case['tree']
        result=build(tree) if case['operation']=='build' else verify(tree,FIXTURES/case['manifest'])
        codes=sorted({f.code for f in result.findings}); match=result.outcome==case['expected_outcome'] and codes==case['expected_findings']
        if match and case.get('expected_manifest'): match=result.manifest==json.loads((FIXTURES/case['expected_manifest']).read_text(encoding='utf-8'))
        print(json.dumps({'case_id':case['case_id'],'outcome':result.outcome,'findings':codes,'suite_match':match},sort_keys=True,separators=(',',':'))); passed=passed and match
    return 0 if passed else 1

def main(argv:Sequence[str]|None=None)->int:
    parser=argparse.ArgumentParser(description='Build or verify deterministic 3D Tiles tree hash manifests.')
    parser.add_argument('--fixtures',action='store_true'); sub=parser.add_subparsers(dest='command')
    b=sub.add_parser('build'); b.add_argument('tree',type=Path); b.add_argument('--output',type=Path)
    v=sub.add_parser('verify'); v.add_argument('tree',type=Path); v.add_argument('manifest',type=Path)
    args=parser.parse_args(argv)
    if args.fixtures:
        if args.command: parser.error('--fixtures cannot be combined with a command')
        return run_fixtures()
    if args.command=='build':
        result=build(args.tree)
        if result.ok:
            payload=json.dumps(result.manifest,sort_keys=True,indent=2)+'\n'
            if args.output: args.output.write_text(payload,encoding='utf-8')
            else: print(payload,end='')
        else: print(json.dumps({'outcome':'ERROR','findings':[{'code':f.code,'field':f.field} for f in result.findings],'scope':SCOPE},sort_keys=True,separators=(',',':')))
        return 0 if result.ok else 1
    if args.command=='verify':
        result=verify(args.tree,args.manifest); print(json.dumps({'outcome':result.outcome,'findings':[{'code':f.code,'field':f.field} for f in result.findings],'scope':SCOPE},sort_keys=True,separators=(',',':'))); return 0 if result.ok else 1
    parser.error('choose build, verify, or --fixtures')

if __name__=='__main__': raise SystemExit(main())
