#!/usr/bin/env python3
"""Validate the projection-only KFM Cross-Domain Seam Register."""
from __future__ import annotations
import argparse, hashlib, json, math
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence
import yaml
from jsonschema import Draft202012Validator, FormatChecker
from yaml.events import AliasEvent
from yaml.resolver import BaseResolver

ROOT=Path(__file__).resolve().parents[3]
REGISTER=ROOT/'control_plane/cross_domain_seam_register.yaml'
SCHEMA=ROOT/'schemas/contracts/v1/governance/cross_domain_seam_register.schema.json'
DOMAIN_REGISTER=ROOT/'control_plane/domain_lane_register.yaml'
DOCTRINE_SHA='44f7e94344cb42b630008eb0bc03a13fcb97dbdfba6f3e56579693a272571e6e'
MAX_BYTES=4*1024*1024;MAX_NODES=8192;MAX_DEPTH=64
LANES_FOR_TEST=('agriculture','archaeology','atmosphere','fauna','flora','geology','habitat','hazards','hydrology','people-dna-land','roads-rail-trade','settlements-infrastructure','soil')
class DuplicateKey(ValueError): pass
class AliasDenied(ValueError): pass
class StrictLoader(yaml.SafeLoader):
    yaml_implicit_resolvers={k:[(tag,rx) for tag,rx in v if tag!='tag:yaml.org,2002:timestamp'] for k,v in yaml.SafeLoader.yaml_implicit_resolvers.items()}
    def compose_node(self,parent,index):
        if self.check_event(AliasEvent): raise AliasDenied
        return super().compose_node(parent,index)
def construct_mapping(loader,node,deep=False):
    loader.flatten_mapping(node);out={}
    for kn,vn in node.value:
        k=loader.construct_object(kn,deep=deep)
        if k in out: raise DuplicateKey
        out[k]=loader.construct_object(vn,deep=deep)
    return out
StrictLoader.add_constructor(BaseResolver.DEFAULT_MAPPING_TAG,construct_mapping)
@dataclass(frozen=True,order=True)
class Finding: code:str; field:str
@dataclass(frozen=True)
class Result:
    findings:tuple[Finding,...]
    @property
    def ok(self): return not self.findings
    @property
    def outcome(self):
        codes={f.code for f in self.findings}
        if not codes:return 'PASS'
        if any(c.startswith(('INPUT_','YAML_','SCHEMA_','REPO_ROOT_')) for c in codes):return 'ERROR_VALIDATOR'
        if codes&{'AUTHORITY_BINDING_MISSING','DECISION_EVIDENCE_MISSING','DOMAIN_REGISTER_UNAVAILABLE','SEAM_CONTRACT_REQUIRED'}:return 'HOLD_UNRESOLVED'
        if codes&{'UNKNOWN_DOMAIN_CONTEXT','SEAM_ID_DUPLICATE','UNEXPECTED_SEAM_ROOT'}:return 'FAIL_NEW_DRIFT'
        return 'FAIL_INVARIANT'
def bounded(value):
    pending=[(value,0)];seen=0
    while pending:
        current,depth=pending.pop();seen+=1
        if seen>MAX_NODES or depth>MAX_DEPTH:return False
        if isinstance(current,float) and not math.isfinite(current):return False
        if isinstance(current,Mapping):pending.extend((v,depth+1) for v in current.values())
        elif isinstance(current,list):pending.extend((v,depth+1) for v in current)
    return True
def load(path):
    try:
        if path.is_symlink():return None,[Finding('INPUT_SYMLINK_DENIED','/')]
        if not path.is_file():return None,[Finding('INPUT_NOT_FILE','/')]
        if path.stat().st_size>MAX_BYTES:return None,[Finding('INPUT_TOO_LARGE','/')]
        value=yaml.load(path.read_text(encoding='utf-8'),Loader=StrictLoader)
    except DuplicateKey:return None,[Finding('YAML_DUPLICATE_KEY','/')]
    except AliasDenied:return None,[Finding('YAML_ALIAS_DENIED','/')]
    except yaml.YAMLError:return None,[Finding('YAML_INVALID','/')]
    except (OSError,UnicodeError):return None,[Finding('INPUT_READ_ERROR','/')]
    if not isinstance(value,dict):return None,[Finding('YAML_ROOT_NOT_OBJECT','/')]
    if not bounded(value):return None,[Finding('YAML_COMPLEXITY_OR_NUMBER_LIMIT','/')]
    return value,[]
def ptr(parts:Iterable[Any]):
    bits=[str(x).replace('~','~0').replace('/','~1') for x in parts]
    return '/'+('/'.join(bits)) if bits else '/'
def schema_findings(value):
    try:
        schema=json.loads(SCHEMA.read_text());Draft202012Validator.check_schema(schema)
        errors=list(islice(Draft202012Validator(schema,format_checker=FormatChecker()).iter_errors(value),101))
    except Exception:return [Finding('SCHEMA_UNAVAILABLE','/')]
    out=[Finding('SCHEMA_INVALID',ptr(e.absolute_path)) for e in sorted(errors[:100],key=lambda e:(ptr(e.absolute_path),str(e.validator)))]
    if len(errors)>100:out.append(Finding('SCHEMA_FINDINGS_TRUNCATED','/'))
    return out
def git_blob(path):
    raw=path.read_bytes();return hashlib.sha1(f'blob {len(raw)}\0'.encode()+raw).hexdigest()
def load_domains(root):
    value,findings=load(root/'control_plane/domain_lane_register.yaml')
    if value is None:return set(),[Finding('DOMAIN_REGISTER_UNAVAILABLE','/domain_lane_register/path')]
    entries=value.get('entries',[])
    ids={e.get('lane_id') for e in entries if isinstance(e,Mapping) and isinstance(e.get('lane_id'),str)}
    return ids,[]
def bindings(value,root):
    out=[];doctrine=value.get('doctrine',{});domain=value.get('domain_lane_register',{})
    for item,key,fn,field in ((doctrine,'sha256',lambda p:'sha256:'+hashlib.sha256(p.read_bytes()).hexdigest(),'/doctrine'),(domain,'git_blob',git_blob,'/domain_lane_register')):
        if not isinstance(item,Mapping):continue
        path=root/str(item.get('path',''))
        if not path.is_file():out.append(Finding('AUTHORITY_BINDING_MISSING',field+'/path'));continue
        try:observed=fn(path)
        except OSError:out.append(Finding('AUTHORITY_BINDING_MISSING',field+'/path'));continue
        if observed!=item.get(key):out.append(Finding('AUTHORITY_DIGEST_MISMATCH',field+'/'+key))
    if not (root/'docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md').is_file():out.append(Finding('DECISION_EVIDENCE_MISSING','/doctrine/decision_ref'))
    return out
def semantic(value,domain_ids):
    out=[];doctrine=value.get('doctrine',{});domain=value.get('domain_lane_register',{})
    if isinstance(doctrine,Mapping) and doctrine.get('sha256')!='sha256:'+DOCTRINE_SHA:out.append(Finding('DOCTRINE_DIGEST_MISMATCH','/doctrine/sha256'))
    if isinstance(domain,Mapping) and domain.get('base_ref')!=value.get('base_ref'):out.append(Finding('BASE_REF_MISMATCH','/domain_lane_register/base_ref'))
    defaults=value.get('defaults',{})
    expected={'interaction_mode':'CITE_ONLY','evidence_rule':'EACH_PARTICIPANT_EVIDENCE_BUNDLE_REQUIRED','source_role_rule':'PRESERVE','sensitivity_rule':'MOST_RESTRICTIVE','policy_rule':'MOST_RESTRICTIVE','release_rule':'EACH_PARTICIPANT_RELEASE_REQUIRED','mutation_authority':False,'publication_authority':False}
    if defaults!=expected:out.append(Finding('DEFAULT_TRUST_BOUNDARY_MISMATCH','/defaults'))
    entries=[e for e in value.get('entries',[]) if isinstance(e,Mapping)];ids=[e.get('seam_id') for e in entries]
    if ids!=sorted(ids):out.append(Finding('SEAMS_NOT_CANONICAL','/entries'))
    if len(ids)!=len(set(ids)):out.append(Finding('SEAM_ID_DUPLICATE','/entries'))
    for i,e in enumerate(entries):
        base=f'/entries/{i}';participants=e.get('participants',[])
        if participants!=sorted(participants):out.append(Finding('PARTICIPANTS_NOT_CANONICAL',base+'/participants'))
        for participant in participants:
            if participant not in domain_ids:out.append(Finding('UNKNOWN_DOMAIN_CONTEXT',base+'/participants'))
        seam_id=e.get('seam_id','')
        if len(participants)==2 and isinstance(seam_id,str) and not seam_id.startswith(participants[0]+'--'+participants[1]+'--'):out.append(Finding('SEAM_ID_PARTICIPANT_MISMATCH',base+'/seam_id'))
        allocations=e.get('authority_allocations',[]);contexts=[a.get('context_id') for a in allocations if isinstance(a,Mapping)]
        if contexts!=sorted(contexts):out.append(Finding('ALLOCATIONS_NOT_CANONICAL',base+'/authority_allocations'))
        if contexts!=participants:out.append(Finding('AUTHORITY_ALLOCATION_INCOMPLETE',base+'/authority_allocations'))
        for j,a in enumerate(allocations):
            if not isinstance(a,Mapping):continue
            owns=a.get('owns',[])
            if owns!=sorted(owns):out.append(Finding('OWNED_CONCEPTS_NOT_CANONICAL',f'{base}/authority_allocations/{j}/owns'))
            if a.get('may_modify_other_context') is not False:out.append(Finding('CROSS_CONTEXT_MUTATION_OVERCLAIM',f'{base}/authority_allocations/{j}/may_modify_other_context'))
        prohibited=e.get('prohibited_inferences',[])
        if prohibited!=sorted(prohibited):out.append(Finding('PROHIBITED_INFERENCES_NOT_CANONICAL',base+'/prohibited_inferences'))
        if e.get('public_join_allowed') is not False:out.append(Finding('PUBLIC_JOIN_OVERCLAIM',base+'/public_join_allowed'))
        if e.get('status')!='HOLD_UNRESOLVED':out.append(Finding('SEAM_STATUS_OVERCLAIM',base+'/status'))
        if e.get('seam_contract_path') is not None:out.append(Finding('SEAM_CONTRACT_OVERCLAIM',base+'/seam_contract_path'))
    return out
def repository(value,root):
    try:r=root.resolve(strict=True)
    except OSError:return [Finding('REPO_ROOT_UNAVAILABLE','/repo_root')]
    out=[]
    for e in value.get('entries',[]):
        if isinstance(e,Mapping) and isinstance(e.get('seam_id'),str) and (r/e['seam_id']).exists():out.append(Finding('UNEXPECTED_SEAM_ROOT','/repo_roots/'+e['seam_id']))
    return out
def validate(path,*,repo_root=ROOT,check_repository=True,check_bindings=True):
    value,out=load(path)
    if value is None:return Result(tuple(sorted(set(out))))
    out+=schema_findings(value)
    if not out:
        domains,domain_findings=load_domains(repo_root);out+=domain_findings
        if not out:out+=semantic(value,domains)
        if check_bindings:out+=bindings(value,repo_root)
        if check_repository:out+=repository(value,repo_root)
    return Result(tuple(sorted(set(out))))
def serialize(path,result):
    try:name=path.resolve().relative_to(ROOT.resolve()).as_posix()
    except Exception:name=path.name
    return json.dumps({'file':name,'findings':[{'code':f.code,'field':f.field} for f in result.findings],'outcome':result.outcome,'scope':'cross-domain-seam-register-projection-only','authority':{'authorizes_join':False,'modifies_domain_records':False,'activates_source':False,'writes_lifecycle_state':False,'authorizes_release':False,'deploys':False,'promotes':False,'publishes':False}},sort_keys=True,separators=(',',':'))
def main(argv:Sequence[str]|None=None):
    p=argparse.ArgumentParser();p.add_argument('path',nargs='?',type=Path,default=REGISTER);p.add_argument('--repo-root',type=Path,default=ROOT);p.add_argument('--no-repository-checks',action='store_true');p.add_argument('--no-binding-checks',action='store_true');a=p.parse_args(argv)
    result=validate(a.path,repo_root=a.repo_root,check_repository=not a.no_repository_checks,check_bindings=not a.no_binding_checks);print(serialize(a.path,result));return 0 if result.ok else 1
if __name__=='__main__':raise SystemExit(main())
