from .constants import FORBIDDEN_SCHEMES, SECRET_KEYS

def _has_secret(x):
    if isinstance(x,dict):
        for k,v in x.items():
            if any(s in str(k).lower() for s in SECRET_KEYS): return True
            if _has_secret(v): return True
    if isinstance(x,list): return any(_has_secret(i) for i in x)
    return False

def _is_net_path(p):
    s=str(p or "")
    return s.startswith(FORBIDDEN_SCHEMES) or ("://" in s)

def validate_manifest(m):
    e=[]
    req=[('local_file_only',True),('no_network',True),('bulk_web_service_loop',False),('publication_allowed',False),('emergency_alert',False),('regulatory_claims_allowed',False),('preliminary_data',True)]
    for k,v in req:
        if m.get(k) is not v: e.append('MANIFEST_INVALID')
    if not m.get('source_doc_refs'): e.append('MANIFEST_INVALID')
    if _has_secret(m): e.append('SECRET_FIELD_DENIED')
    pol=m.get('reconciliation_policy',{})
    if pol.get('deny_publication') is not True or pol.get('deny_exact_sensitive_overlay') is not True: e.append('MANIFEST_INVALID')
    for grp in ('inputs','parse_receipts'):
        for _,v in (m.get(grp) or {}).items():
            if v is None: continue
            if _is_net_path(v): e.append('NETWORK_FORBIDDEN')
    return sorted(set(e))
