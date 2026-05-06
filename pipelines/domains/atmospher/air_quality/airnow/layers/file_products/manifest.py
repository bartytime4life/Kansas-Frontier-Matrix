import json
from .constants import SUPPORTED_PRODUCT_TYPES, FORBIDDEN_SCHEMES, SECRET_KEYS

def _scan_secrets(x):
    if isinstance(x,dict):
        for k,v in x.items():
            lk=k.lower()
            if any(s in lk for s in SECRET_KEYS):
                return True
            if _scan_secrets(v): return True
    elif isinstance(x,list):
        return any(_scan_secrets(v) for v in x)
    return False

def validate_manifest(m):
    errs=[]
    if m.get('product_type') not in SUPPORTED_PRODUCT_TYPES: errs.append('UNSUPPORTED_PRODUCT_TYPE')
    if m.get('local_file_only') is not True or m.get('no_network') is not True: errs.append('NETWORK_FORBIDDEN')
    if m.get('bulk_web_service_loop') is not False: errs.append('BULK_LOOP_DENIED')
    for k,v in [('publication_allowed',False),('emergency_alert',False),('preliminary_data',True)]:
        if m.get(k) is not v: errs.append('MANIFEST_INVALID')
    if not m.get('source_doc_refs'): errs.append('MISSING_PROVENANCE')
    inp=str(m.get('input_file',''))
    if '://' in inp or inp.startswith(FORBIDDEN_SCHEMES): errs.append('NETWORK_FORBIDDEN')
    if _scan_secrets(m): errs.append('SECRET_FIELD_DENIED')
    return errs
